#coding=utf-8
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# 创建数据
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
# print(iris_X[:2, :])
# print(iris_y)
"""
[[ 5.1  3.5  1.4  0.2]
 [ 4.9  3.   1.4  0.2]]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
 """

# 把数据集分为训练集和测试集，其中 test_size=0.3，即测试集占总数据的 30%：
X_train, X_test, y_train, y_test = train_test_split( iris_X, iris_y, test_size=0.3 )
# print(y_train)
"""
[2 1 0 1 0 0 1 1 1 1 0 0 1 2 1 1 1 0 2 2 1 1 1 1 0 2 2 0 2 2 2 2 2 0 1 2 2
 2 2 2 2 0 1 2 2 1 1 1 0 0 1 2 0 1 0 1 0 1 2 2 0 1 2 2 2 1 1 1 1 2 2 2 1 0
 1 1 0 0 0 2 0 1 0 0 1 2 0 2 2 0 0 2 2 2 1 2 0 0 2 1 2 0 0 1 2]
 """

# 建立模型－训练－预测
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)
print(y_predict)
print(y_test)
"""
[2 0 0 1 2 2 0 0 0 1 2 2 1 1 2 1 2 1 0 0 0 2 1 2 0 0 0 0 1 0 2 0 0 2 1 0 1
 0 0 1 0 1 2 0 1]
[2 0 0 1 2 1 0 0 0 1 2 2 1 1 2 1 2 1 0 0 0 2 1 2 0 0 0 0 1 0 2 0 0 2 1 0 1
 0 0 1 0 1 2 0 1]
 """
plt.figure(figsize=(8, 1))
plt.scatter(x=np.arange(y_predict.size),y=y_predict,color='red',label='predict')
plt.scatter(x=np.arange(y_test.size),y=y_test,color='green',label='test')
plt.show()
