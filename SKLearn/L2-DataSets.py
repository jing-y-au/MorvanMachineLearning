#coding=utf-8
from __future__ import print_function
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 导入数据
loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

# 训练模型
model = LinearRegression()
model.fit(data_X, data_y)

# 打印预测值和真实值
print(model.predict(data_X[:4, :]))
print(data_y[:4])

'''
[ 30.00821269  25.0298606   30.5702317   28.60814055]
[ 24.   21.6  34.7  33.4]
'''