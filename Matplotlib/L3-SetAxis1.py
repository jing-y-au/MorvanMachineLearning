#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))       # 设置x坐标轴范围
plt.ylim((-2, 3))       # 设置y坐标轴范围
plt.xlabel('I am x')    # 设置x坐标轴名称
plt.ylabel('I am y')    # 设置y坐标轴名称

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)   # 设置x轴刻度：范围是(-1,2);个数是5
# 使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；
# 对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()