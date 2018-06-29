#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

# 我们之前选cmap的参数时用的是：cmap=plt.cmap.bone，而现在，我们可以直接用单引号传入参数。 origin='lower'代表的就是选择的原点的位置
# 我们在这个链接 ：https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html 可以看到matplotlib官网上对于内插法的不同方法的描述
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')

# 下面我们添加一个colorbar ，其中我们添加一个shrink参数，使colorbar的长度变短为原来的92%
plt.colorbar(shrink=.92)

# 隐藏坐标轴
plt.xticks(())
plt.yticks(())
plt.show()
