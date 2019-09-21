import random
import time


# 定义函数cal_pi，用蒙特卡洛方法计算pi值
def cal_pi(low, high):
    # i参数决定随机实验的次数
    for i in range(low, high):
        counter = 0
        starttime = time.perf_counter()
        for j in range(10 ** i):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            # 如果随机点的位置与（0，0）中心点的距离小于1，认为点落入圆内
            if ((x ** 2 + y ** 2) < 1):
                counter = counter + 1
        endtime = time.perf_counter()
        print('---------------------')
        res = 4 * (counter / (10 ** i))
        timediff = endtime - starttime
        print('pi:{0}'.format(res))
        print('timediff:{0}'.format(timediff))
        print('#####################')


if __name__ == '__main__':
    low = 2
    high = 9
    # print(type(low))
    cal_pi(low, high)
    print('程序结束')
