#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.xlim((-1, 2))       # 设置x坐标轴范围
plt.ylim((-2, 3))       # 设置y坐标轴范围

# 设置x轴,y轴刻度
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)   
plt.yticks([-2, -1.8, -1, 1.22, 3],['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$']) 

# 设置两条线的类型等信息，以及Lable
l1, = plt.plot(x, y1, label='linear line')
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')

#legend将要显示的信息来自于上面代码中的 label. 所以我们只需要简单写下一下代码, plt 就能自动的为我们添加图例
plt.legend(loc='upper right')
plt.show()

# 调整位置和名称
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
plt.show()
# 其中’loc’参数有多种，’best’表示自动分配最佳位置，其余的如下：
'''
 'best' : 0,          
 'upper right'  : 1,
 'upper left'   : 2,
 'lower left'   : 3,
 'lower right'  : 4,
 'right'        : 5,
 'center left'  : 6,
 'center right' : 7,
 'lower center' : 8,
 'upper center' : 9,
 'center'       : 10,
'''