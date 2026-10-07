import numpy

# all 0s matrix
a = numpy.zeros((2, 3))
print(a)

# all 1s matrix

b = numpy.ones((4, 2, 2), dtype='int32')
print(b, b.dtype)

#matrix wiht any other number
c = numpy.full((2, 3), 99)

#random decimal numbers
a_random = numpy.random.rand(4, 2)
print(a_random)

# random integers value
b_random  = numpy.random.randint(7 , size= (3, 3))
print(b_random)

#identity matrix
numpy.identity(5)

output = numpy.ones((5, 5))
z = numpy.zeros((3, 3))
z[1, 1] = 9

output[1:4, 1:4] = z
print(output)

#to copy there is the numpy.copy method