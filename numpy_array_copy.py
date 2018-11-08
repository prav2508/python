from numpy import *
arr = array([2,3,7,4])
arr1 = arr.copy() #deep_copy
arr2 = arr.view() #shallow_copy
arr[1]=10
print(arr1)
print(arr)
print(arr2)
print(id(arr1))
print(id(arr))