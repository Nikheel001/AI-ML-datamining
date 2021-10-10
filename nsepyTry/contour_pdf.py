# contour pdf analysis

import seaborn as sns
from matplotlib import pyplot
from common import stock_data, load_data

def contour_pdf_try(stockData):
    ctr=0
    for i,j in load_data(stockData.values()):
        sns.jointplot(x='High',y='Trades', data=i, kind="kde")
        ctr+=1
        pyplot.title(j)
        pyplot.figure(ctr)
        # sns.jointplot(x='High',y='Turnover', data=i, kind="kde")
        # sns.jointplot(x='High',y='Volume', data=i, kind="kde")
    pyplot.figure(ctr-1)
    pyplot.plot()
    pyplot.show()

contour_pdf_try(stock_data)