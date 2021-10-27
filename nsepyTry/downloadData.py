from datetime import date
from nsepy import get_history
sbin = get_history(symbol='PERSISTENT', start=date(2008,1,1), end=date(2021,10,22))
# sbin.plot()
sbin.to_csv('persistent.csv')
# print(sbin)