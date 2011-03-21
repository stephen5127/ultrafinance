'''
Created on Dec 18, 2010

@author: ppa
'''
from BaseModule import BaseModule
from lib.StockMeasurement import StockMeasurement

class AvgDivProcessor(BaseModule):
    ''' Calculate average and standard deviation '''
    def __init__(self):
        ''' constructor '''
        super(AvgDivProcessor, self).__init__()

    def execute(self, dateValuesDict):
        ''' processing input'''
        super(AvgDivProcessor, self).execute(dateValuesDict)
        for dateValues in dateValuesDict.values():
            stockMeasurement = StockMeasurement(dateValues)
            data = {'days': len(dateValues), 'avg': stockMeasurement.mean(), 'standard deviation': stockMeasurement.std(), \
                    'alpha': stockMeasurement.alpha(), 'beta': stockMeasurement.beta()}

            print data
            return data