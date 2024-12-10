import numpy as np 

# arr=np.array([[1,2,3,4,5],
#               [6,7,8,9,10],
#               [11,12,13,14,15],
#               [16,17,18,19,20]])
# # print(arr[1: :2])
# # print(arr[::-1])
# # print(arr[2,3])


# print(arr*5)

# print(arr+5)

# print(arr-5)

arr3 = np.random.randint(10,50,125).reshape(5,5,5)
print(arr3)
print(arr3.ndim)
print(arr3.shape)
print(arr3)