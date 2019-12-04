# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 随机种子
np.random.seed(19680801)
# 初始化一个二维数组，每行包含10个元素
data = np.random.randn(2, 10)

print(data)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
# 绘制直方图
axs[0, 0].hist(data[0])
# 绘制气泡图
axs[1, 0].scatter(data[0], data[1])
# 绘制折线图
axs[0, 1].plot(data[0], data[1])
# 绘制二维直方图
axs[1, 1].hist2d(data[0], data[1])

plt.show()

if __name__ == '__main__':
    pass
