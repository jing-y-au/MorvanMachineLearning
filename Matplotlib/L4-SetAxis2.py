#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))       # 设置x坐标轴范围
plt.ylim((-2, 3))       # 设置y坐标轴范围

# 设置x轴,y轴刻度
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)   
plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$']) 

# 使用plt.gca获取当前坐标轴信息. 使用.spines设置边框
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x坐标刻度数字或名称的位置：bottom.（所有位置：top，bottom，both，default，none）
ax.xaxis.set_ticks_position('bottom')
# 设置x坐标轴（bottom边框）位置：y=0的位置；（位置所有属性：outward，axes，data）
ax.spines['bottom'].set_position(('data', 0))
# 设置y坐标刻度数字或名称的位置：left.（所有位置：left，right，both，default，none）
ax.yaxis.set_ticks_position('left')
# 设置y坐标轴（left边框）位置：x=0的位置；（位置所有属性：outward，axes，data）
ax.spines['left'].set_position(('data',0))
plt.show()
