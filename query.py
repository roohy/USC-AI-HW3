__author__ = 'roohy'
from implicationUnification import searchImplications
import statics

def queryParser(query):
    pIndex = query.find('(')
    functionName = query[:pIndex]
    inputs = query[pIndex+1:query.rfind(')')]
    if ',' in inputs:
        firstPart = inputs[:inputs.find(',')]
        secondPart = inputs[inputs.find(',')+1:]
        return [functionName,firstPart,secondPart]
    return [functionName,inputs]
def isUnary(query):
    return len(query) == 2
def hasGeneralVar(query):
    for item in statics.variable_list:
        if item in query:
            return item
    return False

'''def unaryChecker(query, function):
    if hasGeneralVar(function):
        return True
    else:
        if query[1] in statics.variable_list:
            return True
        if query[1] == function[1]:
            return True
        else:
            return False
def binaryChecker(query,function):
    if hasGeneralVar(query):
        if query[1] in statics.variable_list:
            if function[1] not in statics.variable_list:
                return False
        if query[2] in statics.variable_list:
            if function[2] not in statics.variable_list:
                return False
'''

def searchFunctions(query):
    if query[0] in statics.unary_functions:
        if hasGeneralVar(statics.unary_functions[query[0]]):
            return True
        else:
            if query[1] in statics.unary_functions[query[0]]:
                return True
            else:
                return False
        return False

    if query[0] in statics.binary_functions:
        for item in statics.binary_functions[query[0]]:
            if hasGeneralVar(query):
                if query[1] in statics.variable_list:
                    if item[0] not in statics.variable_list:
                        continue
                if query[2] in statics.variable_list:
                    if item[1] not in statics.variable_list:
                        continue
            if (query[1] == item[0] or item[0] in statics.variable_list)\
                    and (query[2] == item[1] or item[1] in statics.variable_list):
                return True
            else:
                continue
        return False



    return False


def queryChainer(query):
    if searchFunctions(query):
        return True
    if searchImplications(query):
        return True
    return False
    # if dev is not None:



def queryProcessor(query):
    parsedQuery = queryParser(query)
    result = queryChainer(parsedQuery)
    return result