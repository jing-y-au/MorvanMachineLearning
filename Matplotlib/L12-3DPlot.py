#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 先定义一个图像窗口，在窗口上添加3D坐标轴
fig = plt.figure()
ax = Axes3D(fig)

# 给进 X 和 Y 值，并将 X 和 Y 编织成栅格
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

# plot 3D图像，其中，rstride 和 cstride 分别代表 row 和 column 的跨度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))

# 投影，添加 XY 平面的等高线
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
ax.set_zlim(-2,2)
plt.show()
