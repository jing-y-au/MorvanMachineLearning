#coding=utf-8

import numpy as np

A = np.arange(3,15)
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
         
print(A[3])    # 6

A = np.arange(3,15).reshape((3,4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""
         
print(A[2])         
# [11 12 13 14]

print(A[1][1])      # 8
print(A[1, 1])      # 8

# 用:对一定范围内的元素进行切片操作
print(A[1, 1:3])    # [8 9]

# 逐行打印
for row in A:
    print(row)
"""    
[ 3,  4,  5, 6]
[ 7,  8,  9, 10]
[11, 12, 13, 14]
"""

# 逐列打印
for column in A.T:
    print(column)
"""  
[ 3,  7,  11]
[ 4,  8,  12]
[ 5,  9,  13]
[ 6, 10,  14]
"""

# 逐元素打印
# 脚本中的flatten是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。
# 而flat是一个迭代器，本身是一个object属性
A = np.arange(3,15).reshape((3,4))         
print(A.flatten())   
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)
'''
3
4
...
14
'''