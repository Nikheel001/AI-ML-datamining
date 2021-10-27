from pandas import read_csv
from itertools import cycle
from matplotlib import pyplot

cs =read_csv('haberman.csv')

survivers = cs.groupby('Surv_status')

fig = pyplot.figure()

axis3d = fig.add_subplot(projection='3d')

pyplot.xlabel('Age')
pyplot.ylabel('Op_year')
pyplot.title('Age vs Op_year vs axil_nodes')


axis3d.set_xlabel('Age')
axis3d.set_ylabel('Op_year')
axis3d.set_zlabel('axil_nodes')

colour = cycle('rgb')

for label,Dframe in survivers:
    axis3d.scatter(Dframe['Age'], Dframe['Op_year'], Dframe['axil_nodes'], c=next(colour), label=label)

pyplot.legend()
pyplot.show()