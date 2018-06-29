#coding=utf-8

import numpy as np
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])

c=b**2  # b的平方
# array([0, 1, 4, 9])

c=10*np.sin(a)  
# array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])

print(b<3)  
print('----------')
# array([ True,  True,  True, False], dtype=bool)

a=np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))

print(a)
# array([[1, 1],
#       [0, 1]])

print(b)
print('----------')
# array([[0, 1],
#       [2, 3]])

c_dot = np.dot(a,b) # 矩阵乘法运算
# array([[2, 4],
#       [2, 3]])

c_dot_2 = a.dot(b)
# array([[2, 4],
#       [2, 3]])

a=np.random.random((2,4))
print(a)
# array([[ 0.94692159,  0.20821798,  0.35339414,  0.2805278 ],
#       [ 0.04836775,  0.04023552,  0.44091941,  0.21665268]])
np.sum(a)   # 4.4043622002745959
np.min(a)   # 0.23651223533671784
np.max(a)   # 0.90438450240606416

print("a =",a)
# a = [[ 0.23651224  0.41900661  0.84869417  0.46456022]
# [ 0.60771087  0.9043845   0.36603285  0.55746074]]

print("sum =",np.sum(a,axis=1))
# sum = [ 1.96877324  2.43558896]

print("min =",np.min(a,axis=0))
# min = [ 0.23651224  0.41900661  0.36603285  0.46456022]

print("max =",np.max(a,axis=1))
# max = [ 0.84869417  0.9043845 ]