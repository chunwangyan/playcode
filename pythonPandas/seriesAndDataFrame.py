import pandas as pd
import numpy as np

# series数据类型
dataseries = pd.Series([1, 2, 3], index=['a', 'b', 'c'])

print(dataseries)

# 显示series的key值【索引】
dataseries.keys()
# 显示series的value值【对应取值】
dataseries.values

# series数据增、删、改操作
dataseries['d'] = 10
del dataseries['b']
dataseries['a'] = 100

# series索引切片,"遵循显式优于隐式原则"
# 显式索引
dataseries['a':'d']
dataseries.loc['a':'d']
# 隐式索引
dataseries[0:2]
dataseries.iloc[0:2]

# series掩码过滤
dataseries[(dataseries > 1) & (dataseries < 4)]
dataseries[(dataseries < 2) | (dataseries > 5)]

# dataframe数据类型
workduration = pd.Series([2, 3, 4, 6], index=['xiaozhang', 'xiaoli', 'xiaoma', 'xiaoyan'])
salary = pd.Series([10, 20, 100, 500], index=['xiaozhang', 'xiaoli', 'xiaoma', 'xiaoyan'])
dataframe = pd.DataFrame({'workduration': workduration, 'salary': salary})

# 显示dataframe
print(dataframe)
# 显示df的索引
dataframe.keys()
# 显示df的值数组
dataframe.values

# df的增删改操作
dataframe['avgsalary'] = dataframe['salary'] / dataframe['workduration']
del dataframe['workduration']
dataframe.loc['xiaoma', 'salary'] = 400
dataframe.loc['xiaoma', 'avgsalary'] = 100

# df的索引切片，"遵循显式优于隐式原则"
# 显示索引
dataframe['xiaozhang', 'salary']
dataframe['xiaozhang':'xiaoma']
dataframe.loc['xiaoma':'xiaoyan', 'salary':'avgsalary']
# 隐式索引
dataframe.iloc[0, 1]
dataframe.iloc[:3, 1:]

# df的掩码过滤
dataframe(dataframe.avgsalary > 50, ['salary', 'avgsalary'])
dataframe[dataframe.avgsalary > 50]

# DF算数运算，索引对齐
rng = np.random.RandomState(42)
A = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list('AB'))
B = pd.DataFrame(rng.randint(0, 100, (2, 3)), columns=list('BAC'))

A + B
A - B
A * B
A / B
