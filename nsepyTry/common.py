from pandas import read_csv

stock_data = {'infy':'infy2021.csv', 'tcs':'tcs2021.csv',
'persistent':'persistent2021.csv', 'ofss':'OFSS2021.csv'}

def load_data(csvFileNames):
    for i in csvFileNames:
        yield read_csv(i), i