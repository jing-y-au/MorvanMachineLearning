#coding=utf-8
import pandas as pd
import numpy as np

# Series
s = pd.Series([1,3,6,np.nan,44,1])
print(s)
'''
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
'''
s2 = pd.Series([1,2],dtype=np.float,index=['a','b'])
print(s2)
'''
a    1.0
b    2.0
dtype: float64
'''

# DataFrame
dates = pd.date_range('20160101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
"""
                   a         b         c         d
2016-01-01 -0.253065 -2.071051 -0.640515  0.613663
2016-01-02 -1.147178  1.532470  0.989255 -0.499761
2016-01-03  1.221656 -2.390171  1.862914  0.778070
2016-01-04  1.473877 -0.046419  0.610046  0.204672
2016-01-05 -1.584752 -0.700592  1.487264 -1.778293
2016-01-06  0.633675 -1.414157 -0.277066 -0.442545
"""
# 打印列
print(df['b'])
"""
2016-01-01   -2.071051
2016-01-02    1.532470
2016-01-03   -2.390171
2016-01-04   -0.046419
2016-01-05   -0.700592
2016-01-06   -1.414157
Freq: D, Name: b, dtype: float64
"""
#没有给定index和columns,使用从0开始的默认值
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)
"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""
# 另一种创建DataFrame的方法，单独指定每一列的值
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})              
print(df2)
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
# 查看每列的数据类型，使用dtype属性
print(df2.dtypes)
"""
df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""
# 查看index
print(df2.index)
'''
Int64Index([0, 1, 2, 3], dtype='int64')
'''
# 查看columns
print(df2.columns)
'''
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
'''
# 查看values
print(df2.values)
"""
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']], dtype=object)
"""
# 数据概览
df2.describe()
"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""
# 转置数据
print(df2.T)
"""                   
                     0                    1                    2                    3
A                    1                    1                    1                    1
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00
C                    1                    1                    1                    1
D                    3                    3                    3                    3
E                 test                train                 test                train
F                  foo                  foo                  foo                  foo 
"""

# 对数据的 index 进行排序并输出
print(df2.sort_index(axis=1, ascending=False))
"""
     F      E  D    C          B    A
0  foo   test  3  1.0 2013-01-02  1.0
1  foo  train  3  1.0 2013-01-02  1.0
2  foo   test  3  1.0 2013-01-02  1.0
3  foo  train  3  1.0 2013-01-02  1.0
"""
# 对数据 值 排序输出:
print(df2.sort_values(by='B'))
"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""