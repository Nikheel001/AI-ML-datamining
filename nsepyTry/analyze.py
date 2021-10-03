#basic load and transform

from pandas import read_csv
from matplotlib import pyplot
from datetime import date

df = read_csv('persistent2021.csv')
# df = read_csv('tcs2021.csv')

# print(df.columns)

# print(len(df))

# df['YY'] = [i[:4] for i in df['Date']]
# df['MM'] = [i[5:7] for i in df['Date']]
# df['DD'] = [i[8:] for i in df['Date']]

df = df[df['YY']==2021]

# df.to_csv('infy2021.csv', index=False)
# df.to_csv('tcs2021.csv', index=False)
df.to_csv('persistent2022.csv', index=False)

# pyplot.xlabel('Date')
# pyplot.ylabel('price')

# pyplot.plot(df['Date'],df['High'], label='High')
# pyplot.plot(df['Date'],df['Low'], label='Low')
# # df.plot('Date','High')
# # df.plot('Date','Low')
# pyplot.legend()
# pyplot.show()
