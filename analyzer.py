__author__ = 'roohy'
import statics
from implication import Implication


def implicationAnalyzer(clause):
    pIndex = clause.find('=>')
    firstPart = clause[:pIndex]
    resultPart = clause[pIndex+2:]
    if '\n' in resultPart:
        resultPart = resultPart[:-1]
    #parsing the first part
    parts = firstPart.split('&')
    unary = {}
    binary = {}
    result = resultParser(resultPart)
    for part in parts:
        factAnalyzer(part,unary,binary)

    result = Implication(unary,binary,result)
    statics.implications.append(result)

def resultParser(resultPart ):
    pIndex = resultPart.find('(')
    functionName = resultPart[:pIndex]
    inputs = resultPart[pIndex+1:resultPart.rfind(')')]
    if ',' in inputs:
        firstPart = inputs[:inputs.find(',')]
        secondPart = inputs[inputs.find(',')+1:]
        result = [functionName,firstPart,secondPart]
    else:
        result = [functionName,inputs]
    return result

def factAnalyzer(clause,unary_functions, binary_functions):
    pIndex = clause.find('(')
    functionName = clause[:pIndex]
    inputs = clause[pIndex+1:clause.rfind(')')]
    # print("inputs are theses: ",inputs)
    if ',' in inputs:
        firstPart = inputs[:inputs.find(',')]
        secondPart = inputs[inputs.find(',')+1:]
        if functionName not in binary_functions:
            binary_functions[functionName] = []
        binary_functions[functionName].append((firstPart,secondPart))
    else:
        if functionName not in unary_functions:
            unary_functions[functionName] = []
        unary_functions[functionName].append(inputs)
    #print('updated the unary or binary function result is this')
    #print(unary_functions)
    #print(binary_functions)


def converter(clause):
    if '=>' in clause:
        implicationAnalyzer(clause)
    else:
        factAnalyzer(clause,statics.unary_functions,statics.binary_functions)

def ruleReader(clauses):
    for item in clauses:
        converter(item)
