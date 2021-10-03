# plotting histogram of High

from matplotlib import pyplot
import pandas
import seaborn as sns
import numpy
from common import stock_data, load_data

def plot_histogram(stockData):
    pyplot.xlabel('2021')
    pyplot.ylabel('price')
    for i,j in load_data(stockData.values()):
        pyplot.plot(i['High'],numpy.zeros(len(i)),'o', label=j )
        # pyplot.plot(i['Date'],i['Low'], label='Low')
    pyplot.legend()
    pyplot.show()

def plot_histogram2(stockData):
    # pyplot.xlabel('High')
    # pyplot.ylabel('price')
    temp = pandas.DataFrame()
    for i,j in load_data(stockData.values()):
        temp = temp.append(i[['High','Symbol']])
        # pyplot.plot(i['Date'],i['Low'], label='Low')
    # print(temp.columns)
    sns.FacetGrid(temp,hue='Symbol',height=5).map(sns.histplot, 'High').add_legend()
    # pyplot.legend()
    pyplot.show()

def plot_histogram3(stockData):
    # pyplot.xlabel('High')
    # pyplot.ylabel('price')
    # temp = pandas.DataFrame()
    for i,j in load_data(stockData.values()):
        # temp = temp.append(i[['High','Symbol']])
        # pyplot.plot(i['Date'],i['Low'], label='Low')
        sns.FacetGrid(i[['High', 'Symbol']],hue='Symbol',height=5)\
            .map(sns.histplot, 'High').add_legend()
    # print(temp.columns)
    # pyplot.legend()
    pyplot.show()

# plot_histogram(stock_data)
plot_histogram2(stock_data)
# plot_histogram3(stock_data)