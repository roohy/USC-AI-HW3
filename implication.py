__author__ = 'roohy'

import statics
# from implicationUnification import searchImplications
import copy

class Implication:
    def __init__(self, unaryPreConditions,binaryPreConditions, result):
        self.unaryPreConditions = unaryPreConditions
        self.binaryPreConditions = binaryPreConditions
        self.result = result



    def isEqualQ(self,query):
        if len(self.result) == len(query):
            for i in range(0,len(query)):
                if self.result[i] != query[i]:
                    if query[i] not in statics.variable_list:
                        return False
            return True
        else:
            return False


    def canBeUnified(self,query):
        print('starting can be unified function ',query)
        if len(self.result) == len(query) and self.result[0] == query[0]:
            if len(query) == 2 and self.result[1] in statics.variable_list:
                print('found x and cloning')
                return self.cloneWithX(query[1])
            elif len(query) == 3 :
                if self.result[1] in statics.variable_list and self.result[2] == query[2]:
                    print('found x 2 and cloning')
                    return self.cloneWithX(query[1])
                elif self.result[2] in statics.variable_list and self.result[1] == query[1]:
                    print('found x 2 and cloning ')
                    return self.cloneWithX(query[2])
        return False

    def cloneWithX(self,newX):

        print('x u: ',self.unaryPreConditions,' b: ',self.binaryPreConditions, ' r: ',self.result, ' new x ',newX)
        result = Implication(copy.deepcopy(self.unaryPreConditions),copy.deepcopy(self.binaryPreConditions),copy.deepcopy(self.result))
        for key in result.unaryPreConditions:
            for i in range(0,len(result.unaryPreConditions[key])):
                if result.unaryPreConditions[key][i] in statics.variable_list:
                    result.unaryPreConditions[key][i] = newX
        for key in result.binaryPreConditions:
            newList = []
            for item in result.binaryPreConditions[key]:
                if item[0] in statics.variable_list:
                    newList.append((newX,item[1]))
                elif item[1] in statics.variable_list:
                    newList.append(item[0],newX)
                else:
                    newList.append((item[0],item[1]))
            result.binaryPreConditions[key] = newList

        print('x u: ',result.unaryPreConditions,' b: ',result.binaryPreConditions, ' r: ',result.result)
        return result


    def checkUnary(self,query):
        if query[0] in statics.unary_functions:
            if query[1] in statics.variable_list or query[1] in statics.unary_functions[query[0]]:
                return True
        if self.searchImplications(query):
            return True

        return False

    def checkBinary(self,query):
        if query[0] in statics.binary_functions:
            for item in statics.binary_functions[query[0]]:
                if item[0] == query[1] and item[1] == query[2]:
                    return True
                if item[0] == query[1] and query[2] in statics.variable_list and item[1] not in statics.variable_list:
                    return True
                if item[1] == query[2] and query[1] in statics.variable_list and item[0] not in statics.variable_list:
                    return True
        if self.searchImplications(query):
             return True
        return False

    def checkPreCons(self):
        for con in self.unaryPreConditions:
            for item in self.unaryPreConditions[con]:
                if not self.checkUnary([con,item]):
                    return False
        for con in self.binaryPreConditions:
            for item in self.binaryPreConditions[con]:
                if not self.checkBinary([con,item[0],item[1]]):
                    return False
        return True



    def searchImplications(self,query):
        for imp in statics.implications:
            if imp.isEqualQ(query) and imp.checkPreCons():
                return True
            elif imp.canBeUnified(query):
                if imp.canBeUnified(query).checkPreCons():
                    return True

        return False