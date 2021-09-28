from pandas import read_csv
from matplotlib import pyplot
from seaborn import pairplot

df = read_csv('Iris.csv')

#iris = df.groupby('Species')
#seaborn.set_style('whitegrid')

pairplot(df, hue='Species', height=2)

pyplot.show()

# pyplot.xlabel('PetalLengthCm')
# pyplot.ylabel('PetalWidthCm')
# pyplot.title('PetalLengthCm vs PetalWidthCm')

# for label,Dframe in iris:
#     pyplot.plot(Dframe['PetalLengthCm'], Dframe['PetalWidthCm'], 'o', label=label)

# # SepalLengthCm SepalWidthCm PetalLengthCm PetalWidthCm Species
# pyplot.legend()
# pyplot.show()

