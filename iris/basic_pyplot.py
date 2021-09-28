from matplotlib import pyplot
from numpy import arange

base = arange(20)

arr = [i**2 for i in base]
brr = [i**2.3 for i in base]
crr = [i for i in base]

pyplot.plot(base, arr, 'g^', label = 'y = x**2')
pyplot.plot(base, brr, 'rs', label = 'y = x**3')
pyplot.plot(base, base**2.5, 'bo', label = 'y = x')
pyplot.plot(base, base, label = 'y = x')
pyplot.xlabel("X")
pyplot.ylabel("Y")
pyplot.title("plotTest")
pyplot.grid()
pyplot.show()