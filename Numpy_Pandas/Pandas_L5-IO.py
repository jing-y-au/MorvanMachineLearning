#coding=utf-8
import pandas as pd

# 读取csv
data = pd.read_csv('student.csv')

# 打印出data
print(data)

# 将资料存取成pickle
data.to_pickle('student.pickle')