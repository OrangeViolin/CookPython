import numpy as np
# arr1 = np.array([2,3,4])
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([2.3,3.4,4.5])
# print(arr2)
# print(arr2.dtype)
#
# print(arr2+arr1)
#
# print(arr2 * 10)
#
# data = [[1,2,3],[4,5,6],[7,8,9]]
# arr3 = np.array(data)
# print(arr3)

# print(np.zeros(10))
# # print(np.ones((3,9)))
# # print(np.empty((2,3,2)))

arr4 = np.arange(10)
arr4[5:8] = 10
print(arr4)
arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4.dtype)