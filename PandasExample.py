import pandas
import numpy

# Creating empty series
#ser = pandas.ser()
#print("Pandas Series: ", ser)

# simple array
data = numpy.array(['g', 'e', 'e', 'k', 's'])

ser = pandas.Series(data)
print("Pandas Series:\n", ser)