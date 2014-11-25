__author__ = 'roohy'


def ReadFile(filename):
    FILE = open( filename, 'r')
    query = FILE.readline()
    clauseNumber = (int)(FILE.readline())

    clauses = []
    for i in range(0,clauseNumber):
        clauses.append(FILE.readline())
        print("rule imported ", clauses[len(clauses)-1])
    return [query,clauses]

def WriteFile(filename , message):
    FILE = open(filename,'w')
    FILE.write(message)
    return

