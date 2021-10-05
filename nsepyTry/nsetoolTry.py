from nsetools import Nse
from numpy import array
import csv

nse = Nse()

[print(i) for i in nse.get_top_gainers()]
print("======================================================")
[print(i) for i in nse.get_top_losers()]
print("======================================================")

indexList = array(nse.get_index_list())

with open('nse_codes.csv', 'w') as fptr:
    csv.writer(fptr).writerows(nse.get_stock_codes().items())

indexList.tofile('indexList.csv', sep=',')