from pandas import read_csv
from matplotlib import pyplot
from itertools import cycle

df = read_csv('Iris.csv',sep=',')

iris = df.groupby('Species')

fig = pyplot.figure()

axis3d = fig.add_subplot(projection='3d')

pyplot.xlabel('SepalWidthCm')
pyplot.ylabel('PetalLengthCm')
pyplot.title('SepalWidthCm vs PetalLengthCm vs PetalWidthCm')


axis3d.set_xlabel('SepalWidthCm')
axis3d.set_ylabel('PetalLengthCm')
axis3d.set_zlabel('PetalWidthCm')

colour = cycle('rgb')

for label,Dframe in iris:
    axis3d.scatter(Dframe['SepalWidthCm'], Dframe['PetalLengthCm'], Dframe['PetalWidthCm'], c=next(colour), label=label)

pyplot.legend()
pyplot.show()