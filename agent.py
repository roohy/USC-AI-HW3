__author__ = 'roohy'
from FileOperations import ReadFile,WriteFile
from statics import *
from analyzer import *
import query


inputs = ReadFile('input.txt')
ruleReader(inputs[1])
result = query.queryProcessor(inputs[0])
print('result is ', result, '  for query ',inputs[0])
outputFile = 'output.txt'

WriteFile(outputFile, ('TRUE' if result else 'FALSE'))