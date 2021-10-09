from datetime import date
from nsepy import get_history
from pandas import read_csv

sym='M&MFIN'

def download_data(symbol):
    df = get_history(symbol=symbol, start=date(2008,1,1), end=date(2021,10,5))
    # export
    if len(df)>0:
        df.to_csv(symbol+'.csv')
    else:
        print("incorrect symbol")

def load_and_filter(symbol):
    df = read_csv(symbol+'.csv')

    df['YY'] = [int(i[:4]) for i in df['Date']]
    df['MM'] = [int(i[5:7]) for i in df['Date']]
    df['DD'] = [int(i[8:]) for i in df['Date']]
    
    # # filter
    # df = df[df['YY']==2021]

    df2021 = df[df.YY == 2021]
    # [print(type(i)) for i in df['YY'].head()]
    df2021.to_csv(symbol+'2021.csv', index=False)

download_data(sym)
# load_and_filter(sym)