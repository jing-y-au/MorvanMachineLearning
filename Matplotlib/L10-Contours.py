#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

# 数据集即三维点 (x,y) 和对应的高度值，共有256个点。
# 高度值使用一个 height function f(x,y) 生成。 
# x, y 分别是在区间 [-3,3] 中均匀分布的256个值，并用meshgrid在二维平面中将每一个x和每一个y分别对应起来，编织成栅格
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

# 接下来使用函数plt.contourf进行颜色填充。
# 位置参数分别为：X, Y, f(X,Y)。透明度0.75，并将 f(X,Y) 的值对应到color map的暖色组中寻找对应颜色
# 8代表等高线的密集程度，这里被分为10个部分。如果是0，则图像被一分为二
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

# 接下来使用plt.contour函数进行等高线绘制
# 位置参数为：X, Y, f(X,Y)。颜色选黑色，线条宽度选0.5
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# 最后加入Label，inline控制是否将Label画在线里面，字体大小为10
plt.clabel(C, inline=True, fontsize=10)
# 隐藏坐标轴
plt.xticks(())
plt.yticks(())

plt.show()