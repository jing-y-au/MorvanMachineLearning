#coding=utf-8
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

print(model.coef_)      # 斜率
print(model.intercept_) # 截距
"""
[ -1.07170557e-01   4.63952195e-02   2.08602395e-02   2.68856140e+00
  -1.77957587e+01   3.80475246e+00   7.51061703e-04  -1.47575880e+00
   3.05655038e-01  -1.23293463e-02  -9.53463555e-01   9.39251272e-03
  -5.25466633e-01]
36.4911032804
"""
print(model.get_params())
"""
{'copy_X': True, 'normalize': False, 'n_jobs': 1, 'fit_intercept': True}
"""
print(model.score(data_X, data_y)) # R^2 coefficient of determination
"""
0.740607742865
"""