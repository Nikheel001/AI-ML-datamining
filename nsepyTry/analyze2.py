#basic date vs High graph

from matplotlib import pyplot
from common import stock_data, load_data

def plot_it(stockData):
    pyplot.xlabel('Date')
    pyplot.ylabel('price')
    for i,j in load_data(stockData.values()):
        pyplot.plot(i['Date'],i['High'], label=j)
        # pyplot.plot(i['Date'],i['Low'], label='Low')
    pyplot.legend()
    pyplot.show()


plot_it(stock_data)
