from datetime import date
from nsepy import get_history
sbin = get_history(symbol='PERSISTENT', start=date(2015,1,1), end=date(2021,9,17))
# sbin.plot()
sbin.to_csv('persistent.csv')
# print(sbin)