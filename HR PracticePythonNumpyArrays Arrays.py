import numpy

def arrays(arr):
    return numpy.array(numpy.flip(arr),float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)