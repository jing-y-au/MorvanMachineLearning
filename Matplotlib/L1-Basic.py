#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1

# 使用plt.figure定义一个图像窗口. 使用plt.plot画(x ,y)曲线. 使用plt.show显示图像
plt.figure()
plt.plot(x, y)
plt.show()