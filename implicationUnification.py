__author__ = 'roohy'

from implication import Implication
import statics



def searchImplications(query):
    print('starting Search Implication')
    for imp in statics.implications:
        if imp.isEqualQ(query) and imp.checkPreCons():
            return True
        elif imp.canBeUnified(query):
            if imp.canBeUnified(query).checkPreCons():
                return True

    return False

