import pandas
from common import stock_data, load_data
import seaborn as sns
from matplotlib import pyplot

arr = pandas.concat([i for i,j in load_data(stock_data.values())])

def boxplotTry(stockData):
    sns.boxplot(x='Symbol', y='High',data=stockData)
    pyplot.grid()
    pyplot.plot()
    pyplot.show()

def violinplotTry(stockData):
    sns.violinplot(x='High', y='Symbol',data=stockData, size = 8)
    pyplot.grid()
    pyplot.plot()
    pyplot.show()

# boxplotTry(arr)
violinplotTry(arr)