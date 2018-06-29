#coding=utf-8

import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])

# ------------------------------------
# np.vstack()   
C = np.vstack((A,B))  # vertical stack
print(C)    
# [[1,1,1]
#  [2,2,2]]
print(A.shape,C.shape)
# (3,) (2,3)

# ------------------------------------
# np.hstack()
D = np.hstack((A,B))       # horizontal stack
print(D)
# [1,1,1,2,2,2]
print(A.shape,D.shape)
# (3,) (6,)

# ------------------------------------
# np.newaxis()
# 将具有3个元素的array转换为1行3列
print(A[np.newaxis,:])
# [[1 1 1]]
print(A[np.newaxis,:].shape)
# (1,3)

# 将具有3个元素的array转换为3行1列
print(A[:,np.newaxis])
# [[1]
# [1]
# [1]]
print(A[:,np.newaxis].shape)
# (3,1)

# 将两个数组转换成竖列并纵向合并
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
D = np.hstack((A,B))   # horizontal stack
print(D)
# [[1 2]
# [1 2]
# [1 2]]
print(A.shape,D.shape)
# (3,1) (3,2)

# ------------------------------------
# np.concatenate()
# 当你的合并操作需要针对多个矩阵或序列时，借助concatenate函数可能会让你使用起来比前述的函数更加方便
# axis参数很好的控制了矩阵的纵向或是横向打印，相比较vstack和hstack函数显得更加方便
C = np.concatenate((A,B,B,A),axis=0)

print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A,B,B,A),axis=1)
print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""