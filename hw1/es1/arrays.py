import numpy

def arrays(arr):
    array=numpy.array(arr,dtype=numpy.float)
    return array[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)