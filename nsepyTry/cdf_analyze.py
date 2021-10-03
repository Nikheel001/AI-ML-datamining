# Cumulative Distribution Function

from matplotlib.figure import Figure
from pandas import read_csv
from matplotlib import pyplot
from math import ceil, floor
# import pandas
# import seaborn as sns
import numpy

stock_data = {'infy':'infy2021.csv', 'tcs':'tcs2021.csv',
'persistent':'persistent2021.csv', 'ofss':'OFSS2021.csv'}

def getPlotPlacement(count, fig: Figure):
    tmp = count**0.5
    r = floor(tmp)
    c = ceil(tmp)
    ax = fig.subplots(nrows = r, ncols = c)
    for i in range(r):
        for j in range(c):
            yield ax[i,j]

def load_data(csvFileNames):
    for i in csvFileNames:
        yield read_csv(i), i

def cdf_histogram(stockData):
    pyplot.xlabel('High')
    pyplot.ylabel('price')
    n_stocks = len(stockData)
    fig = pyplot.figure(1)
    placement = getPlotPlacement(n_stocks, fig)
    for i,label in load_data(stockData.values()):
        counts,weights = numpy.histogram(i['High'], bins=10, density=True)
        pdf = counts/sum(counts)
        cdf = numpy.cumsum(pdf)
        place = next(placement)
        place.plot(weights[1:], pdf, label=label+'_PDF')
        place.plot(weights[1:], cdf, label=label+'_CDF')
        place.legend()
    pyplot.show()

def cdf_histogram(stockData):
    pyplot.xlabel('High')
    pyplot.ylabel('price')
    j = iter(range(len(stockData)))
    for i,label in load_data(stockData.values()):
        pyplot.figure(next(j)+1)
        counts,weights = numpy.histogram(i['High'], bins=10, density=True)
        pdf = counts/sum(counts)
        cdf = numpy.cumsum(pdf)
        pyplot.plot(weights[1:], pdf, label=label+'_PDF')
        pyplot.plot(weights[1:], cdf, label=label+'_CDF')
        pyplot.legend()
    pyplot.show()


cdf_histogram(stock_data)