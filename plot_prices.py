import clean_data
import convert
import numpy as np
import matplotlib.pyplot as plt
import time

# Getting the index associated to the biggest moment before t
def binarySearch(t, dates, times, unit):
    start=0
    end=len(dates)-1
    n=-1
    
    while start<=end:
        mid=(start + end) // 2
        midTime=convert.getTimeFromReference(dates[mid],times[mid],unit)
        
        if midTime>t:
            end=mid-1
        else:
            n=mid
            start=mid+1
    
    return n

# Plotting the price history of the underlaying value (price of a share, 
# value of an index, ...) from a start moment to a final moment   
def plotPrices(startDate,startTime,endDate,endTime,priceType,symbol,unit):
    
    data=clean_data.getData(symbol)
        
    # We choose the price type (OPEN, CLOSE, HIGH or LOW) we are dealing with
    S=data.getColumn(priceType)
            
    dates=data.getColumn("DATE")
    times=data.getColumn("TIME")
    
    # Find s such that time t_s is the biggest time such that t_s<=start time
    startTimeMeasure=convert.getTimeFromReference(startDate,startTime,unit)
    s=binarySearch(startTimeMeasure,dates,times,unit)
    
    # Find e such that time t_e is the biggest time such that t_e<=end time
    endTimeMeasure=convert.getTimeFromReference(endDate,endTime,unit)
    e=binarySearch(endTimeMeasure,dates,times,unit) 
    
    # Sclicing to shape the price interval that we want to plot
    S=S[s:e+1] 
    
    # Time gap, expressed according to the choosen unit
    diffTime=endTimeMeasure-startTimeMeasure
    
    timeLine=np.linspace(0,int(diffTime),e-s+1)
    
    plt.plot(timeLine, S)
    literalStartDateTime=convert.getLiteralDateAndTime(startDate, startTime)
    literalEndDateTime=convert.getLiteralDateAndTime(endDate, endTime)
    plt.xlabel('t: {} from {} to {}'.format(unit,literalStartDateTime,literalEndDateTime))
    symbolNumbers = {
        "AAPL": 0,
        "AMZN": 1,
        "DJIA": 2,
        "BTC": 3
    }
    inTitles=['Apple Share Prices',
              'Amazon Share Prices',
              'Dow Jones Stock Market Performance',
              'Bitcoin Price History']
    plt.title('{} (USD)   ({} prices)'.format(inTitles[symbolNumbers[symbol]],priceType.lower()))
    plt.ylabel('Value at time t')
    plt.grid(True)
    plt.show()
    
    
    
    
    
                    # # # # # Applications # # # # #
                    
                    
                    
                    
                    

# Plotting and computing the execution time
startTime=time.time()
plotPrices("20200105","101000","20200415","111000","OPEN","BTC","days")
endTime=time.time()
executionTime=endTime-startTime
print("Execution time:",executionTime,"seconds")





# When start time and end time are too close, the plot is not that convenient 
# with "days" unit, that is quite understandable, regarding the construction 
# of s and e
# However, the plots are all right when one precise "hours" or "min" for unit

# One can choose to work on open, close, high or low prices.
# The results are quite similar, but it is then possible to choose the price 
# type that we want












