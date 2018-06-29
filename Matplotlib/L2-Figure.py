#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# 使用plt.figure定义一个图像窗口. 使用plt.plot画(x ,y1)曲线.
plt.figure()
plt.plot(x, y1)
plt.show()

# 使用plt.figure定义一个图像窗口：编号为3；大小为(8, 5).
# 画(x ,y2)直线 和 (x ,y1)曲线
# 曲线的颜色属性(color)为红色;曲线的宽度(linewidth)为1.0；曲线的类型(linestyle)为虚线
plt.figure(num=3, figsize=(8, 5),)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()