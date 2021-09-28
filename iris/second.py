from os import read
from pandas import read_csv
from matplotlib import pyplot

df = read_csv('Iris.csv')

iris = df.groupby('Species')

# setosa = iris.get_group('Iris-setosa')
# versicolor = iris.get_group('Iris-versicolor')
# virginica= iris.get_group('Iris-virginica')

pyplot.xlabel('PetalLengthCm')
pyplot.ylabel('PetalWidthCm')
pyplot.title('PetalLengthCm vs PetalWidthCm')

for label,Dframe in iris:
    pyplot.plot(Dframe['PetalLengthCm'], Dframe['PetalWidthCm'], 'o', label=label)

# SepalLengthCm SepalWidthCm PetalLengthCm PetalWidthCm Species
pyplot.legend()
pyplot.show()

