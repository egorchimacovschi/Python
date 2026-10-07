import numpy

a = numpy.array([[1, 2, 3, 4, 5, 6, 7], [10, 11, 12, 13, 14, 15 ,16]])
print (a)
# get a specific item
print(a[1, 5])
# get a specific row
print(a[0, :])
#get a specific column
print(a[:, 3])

# gettign a little more fancy [startingindex:endindex:stepsize]
a[0, 1:2:-2]
#changing the element
a[1,5] = 20
print(a)
a[:,2] = [1,2]
print(a)
b = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)

print(b[0, 1, 1])
#replace 
b[:, 1, :] = [[9, 9], [9, 9]]
print(b)