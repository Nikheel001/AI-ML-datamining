import pandas
from matplotlib import pyplot
from pandas.core import groupby

df = pandas.read_csv('Iris.csv')

iris = df.groupby('Species')

setosa = iris.get_group('Iris-setosa')
versicolor = iris.get_group('Iris-versicolor')
virginica= iris.get_group('Iris-virginica')

# print(df.columns)

pyplot.xlabel('SepalLengthCm')
pyplot.ylabel('SepalWidthCm')
pyplot.title('SepalLengthCm vs SepalWidthCm 2D')

pyplot.plot(setosa['SepalWidthCm'], setosa['SepalLengthCm'], 'ro', label='setosa')
pyplot.plot(versicolor['SepalWidthCm'],versicolor['SepalLengthCm'], 'bo', label='versicolor')
pyplot.plot(virginica['SepalWidthCm'],virginica['SepalLengthCm'], 'go', label='virginica')
pyplot.legend()
# 'SepalWidthCm'
pyplot.show()