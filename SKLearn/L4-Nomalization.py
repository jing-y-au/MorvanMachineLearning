#coding=utf-8
from sklearn import preprocessing #标准化数据模块
import numpy as np

#建立Array
a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)

#将normalized后的a打印出
print(preprocessing.scale(a))
# [[ 0.         -0.85170713 -0.55138018]
#  [-1.22474487 -0.55187146 -0.852133  ]
#  [ 1.22474487  1.40357859  1.40351318]


# 另一种方法，可以保存训练集中的参数（均值、方差）直接使用其对象转换测试集数据
scaler = preprocessing.StandardScaler().fit(a)
scaler.transform(a)