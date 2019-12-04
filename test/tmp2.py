import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.randn(20)
bins = np.linspace(-5, 5, 20)

print("----------横轴坐标-------------")
print(x)
print("----------纵轴坐标-------------")
print(bins)

plt.hist(x, bins, histtype='step')

plt.show()

if __name__ == '__main__':
    pass
