import numpy

a = numpy.array([1, 2, 3, 4])
print(a - 2)
print(a + 2)
print(a * 2)
print(a / 2)
print(a ** 2)
#cos tg and others
print(numpy.sin(a))
\

#Linear Algebra
a = numpy.ones((2, 3))
print(a)
b = numpy.full((3, 2), 2)
print(b)
print(numpy.matmul(a, b))

c = numpy.identity(3)
print(numpy.linalg.det(c))