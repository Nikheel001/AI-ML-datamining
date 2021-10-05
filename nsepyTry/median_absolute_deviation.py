# Median absolute deviation
# alternative to st_deviation

from numpy import median
from common import stock_data, load_data
from statsmodels import robust

def mad(data):
    u = median(data)
    update = [abs(i-u) for i in data]
    # update.sort()
    c =  0.6745
    return median(update)/c

def madObservation(stockData):
    for i, label in load_data(stockData.values()):
        print(robust.mad(i['High']))
        print(mad(i['High']))

madObservation(stock_data)