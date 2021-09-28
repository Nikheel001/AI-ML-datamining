from pandas import read_csv
from matplotlib import pyplot

stock_data = {'infy':'infy2021.csv', 'tcs':'tcs2021.csv', 'persistent':'persistent2021.csv', 'ofss':'OFSS2021.csv'}

def load_data(csvFileNames):
    for i in csvFileNames:
        yield read_csv(i), i

def plot_it(stockData):
    pyplot.xlabel('Date')
    pyplot.ylabel('price')
    for i,j in load_data(stockData.values()):
        pyplot.plot(i['Date'],i['High'], label=j)
        # pyplot.plot(i['Date'],i['Low'], label='Low')
    pyplot.legend()
    pyplot.show()


plot_it(stock_data)
