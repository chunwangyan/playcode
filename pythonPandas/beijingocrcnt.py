import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据文件
filepath = "/Users/yanchw/Desktop/codes/python/playcode/dataSet/ocrrecordcnt.csv"
ocrfile = pd.read_csv(filepath)
# print(ocrfile["mt"])


# 绘制折线图
plt.plot(ocrfile["mt"], ocrfile["cnt"])
plt.show()

if __name__ == "__main__":
    pass
