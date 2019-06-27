import math
import random


# 折半查找法【适用于各种有序列表类型】
# 算法特点：稳定，适用性较好
# 算法思路：待查找的集合必须是有序的向量存储集合，通过比较判定目标值的区间，逐步缩小查找范围，时间复杂度（O(logn)）
# 本算法的实现有一个bug,当数据足够多，超出类型的最大值时，程序会发生内存溢出【(down + up) / 2】
# 改进算法：(down + up) / 2 修改为 移位运算 (down + up) >> 1
def binarysearch(l, mb):
    # 初始化目标值
    m = mb
    # 初始化返回结果集
    result = {}
    # 边界判断，若查找列表为空，不做比较，直接输出结果
    if len(l) == 0:
        result['address'] = -1
        result['comp_num'] = 0
        return result
    # 查询列表低值索引
    down = 0
    # 查询列表高值索引
    up = len(l) - 1
    # 查询列表比较值索引
    mid = math.ceil((down + up) >> 1)
    # 记录查询比较次数
    comp_num = 0
    # 值域判断，如果目标值比数组最小值小或者比最大值大，不做比较，直接输出结果
    if m < l[down] or m > l[up]:
        result['address'] = -1
        result['comp_num'] = 0
        return result
    while down <= up:
        # 第一个定位到目标值位置找到，无法找到其他与目标值重复的目标值位置
        if m == l[mid]:
            comp_num += 1
            result['comp_num'] = comp_num
            result['address'] = mid
            return result
        # 目标值比当前比较值小，将高值索引前移至当前比较值
        elif m < l[mid]:
            up = mid - 1
            # 结果值向上取整
            mid = math.ceil((down + up) >> 1)
            comp_num += 1
            result['comp_num'] = comp_num
        # 目标值比当前比较值大，将低值索引后移至当前比较值
        else:
            down = mid + 1
            mid = math.ceil((down + up) >> 1)
            comp_num += 1
            result['comp_num'] = comp_num
    # 经过遍历查找，目标值在list中未找到，返回错误码
    if down > up:
        result['address'] = -1
        return result


# 重构二分查找算法
# 解决边界判断导致错误的bug
# 逻辑判断更加简洁，代码更清晰
# 代码中绿色的波浪线表示单词拼写错误
def binarysearchv2(l, mb):
    # 判断list是否为空
    if len(l) == 0:
        resultnull = dict()
        resultnull['comp_num'] = 0
        resultnull['address'] = -1
        return resultnull
    # 若带查找的list不为空
    else:
        m = mb
        # 初始化待查找list的高、低值索引
        down = 0
        up = len(l) - 1
        # 判断目标值是否超过了待查找list的值域
        if m < l[down] or m > l[up]:
            resultout = dict()
            resultout['comp_num'] = 0
            resultout['address'] = -1
            return resultout
        # 目标值在待查找list的值域以内
        else:
            # 初始化中间值的索引
            mid = math.ceil(calculatemid(down, up))
            # 初始化返回dict，用于信息输出
            resultin = dict()
            comp_num = 0
            # 当低值索引不大于高值索引时，程序循环执行
            # 换句话说，当低值索引大于高值索引时，程序跳出while循环
            while down <= up:
                # 找到list中目标值的索引位置，程序返回
                if m == l[mid]:
                    comp_num += 1
                    resultin['comp_num'] = comp_num
                    resultin['address'] = mid
                    return resultin
                # 目标值小于中间值，缩小一半查找范围，修改高值索引
                if m < l[mid]:
                    up = mid - 1
                    mid = math.ceil(calculatemid(down, up))
                    comp_num += 1
                    resultin['comp_num'] = comp_num
                # 目标值大于中间值，缩小一半查找范围，修改低值索引
                if m > l[mid]:
                    down = mid + 1
                    mid = math.ceil(calculatemid(down, up))
                    comp_num += 1
                    resultin['comp_num'] = comp_num
            # 目标值未找到，输出错误信息
            resultin['address'] = -1
            return resultin


# 重构二分查找方法，适用待查找元素在列表重复的情形
# 在字典里封装一个list存储所有带查找元素的索引
def binarysearchv3(l, mb):
    # 判断list是否为空
    if len(l) == 0:
        resultnull = dict()
        resultnull['comp_num'] = 0
        resultnull['address'] = -1
        return resultnull
    # 若待查找的list不为空，继续判断并查找目标值
    else:
        m = mb
        # 初始化待查找list的高、低值索引
        down = 0
        up = len(l) - 1
        # 判断目标值是否超过了待查找list的值域
        if m < l[down] or m > l[up]:
            resultout = dict()
            resultout['comp_num'] = 0
            resultout['address'] = -1
            return resultout
        # 目标值在待查找list的值域以内
        else:
            # 初始化中间值的索引
            mid = math.ceil(calculatemid(down, up))
            # 初始化返回dict，用于信息输出
            resultin = dict()
            comp_num = 0
            # 初始化一个list，用于存储找到的重复目标值的位置
            res = []
            # 当低值索引不大于高值索引时，程序循环执行
            while down <= up:
                # 找到list中目标值的索引位置，程序结束，返回结果
                if m == l[mid]:
                    # 查找出list中出现的最小的目标值索引
                    while mid > 0 and l[mid - 1] == m:
                        mid = mid - 1
                        comp_num += 1
                        resultin['comp_num'] = comp_num
                    # 顺序查找与目标值想等的多个list索引位置，并记录下来
                    while mid > 0 and l[mid] == m:
                        res.append(mid)
                        mid = mid + 1
                        comp_num += 1
                        resultin['comp_num'] = comp_num
                    # 输出所有与目标值相等的列表元素索引
                    resultin['address'] = res
                    return resultin
                # 目标值小于中间值，缩小一半查找范围，修改上索引值
                if m < l[mid]:
                    up = mid - 1
                    mid = math.ceil(calculatemid(down, up))
                    comp_num += 1
                    resultin['comp_num'] = comp_num
                # 目标值大于中间值，缩小一半查找范围，修改下索引值
                if m > l[mid]:
                    down = mid + 1
                    mid = math.ceil(calculatemid(down, up))
                    comp_num += 1
                    resultin['comp_num'] = comp_num
            # 目标值未找到，输出错误信息
            resultin['address'] = res
            return resultin


# 二分查找算法中求中间值的方法【本方法需要进行边界测试】
# 独立出来此方法，一是为了便于测试，而是未来使代码方便阅读
# 这里的除法运算使用位移符来实现，避开内存溢出bug
def calculatemid(val1, val2):
    return (val1 + val2) >> 1


# 顺序查找法
# 算法特点：不稳定，不要求查找列表有序，适用性最好
# 算法思路：遍历列表所有元素，查找与目标值相等的元素，不要求列表元素有序，不要求列表元素固定数据类型，算法事件复杂度（O(n)）
def sequencesearch(l, mb):
    m = mb
    # 记录比较次数
    comp_num = 0
    # 记录返回结果集
    result = dict()
    # 边界判断，不比较直接输出结果
    if len(l) == 0:
        result['comp_num'] = 0
        result['address'] = -1
        return result
    for i in range(len(l)):
        if m == l[i]:
            comp_num += 1
            result['comp_num'] = comp_num
            result['address'] = i
            return result
        else:
            comp_num += 1
            result['comp_num'] = comp_num
            i += 1
    # 目标值未找到，返回错误码
    result['address'] = -1
    return result


# 差值查找法【二分查找的改进型，适用于查找表值分布均匀,查找集合比较大】
# 算法特点：不稳定，特殊情况下比二分查找效率高
# 算法思路：根据目标值在查找范围的分布区间取比较值，逐步缩小查找范围，以期减少查询比较次数
def insertsearch(l, mb):
    m = mb
    # 查询列表低值索引
    down = 0
    # 查询列表高值索引
    up = len(l) - 1
    # 返回结果集
    result = dict()
    # 边界判断，不比较直接输出结果
    if len(l) == 0:
        result['address'] = -1
        result['comp_num'] = 0
        return result
    # 查询列表比较值索引[索引点选择依据是查找值在查找区间的分布情况]
    if l[up] - l[down] > 0:
        mid = down + math.floor((m - l[down]) / (l[up] - l[down]) * (up - down))
    else:
        mid = math.ceil((down + up) / 2)
    # 记录查询比较次数
    comp_num = 0
    if m < l[down] or m > l[up]:
        result['comp_num'] = 0
    # 边界判断，如果查找值超出查找范围，不比较，直接跳出循环
    while down <= up:
        # 目标值找到，查找并输出第一个被定位的目标值
        if m == l[mid]:
            comp_num += 1
            result['comp_num'] = comp_num
            result['address'] = mid
            return result
        # 目标值比当前比较值小，将高值索引前移至当前比较值
        elif m < l[mid]:
            comp_num += 1
            up = mid - 1
            # 结果值向下取整
            if l[up] - l[down] > 0:
                mid = down + math.floor((m - l[down]) / (l[up] - l[down]) * (up - down))
            else:
                mid = math.ceil((down + up) / 2)
            result['comp_num'] = comp_num
        # 目标值比当前比较值大，将低值索引后移至当前比较值
        else:
            comp_num += 1
            down = mid + 1
            if l[up] - l[down] > 0:
                mid = down + math.floor((m - l[down]) / (l[up] - l[down]) * (up - down))
            else:
                mid = math.ceil((down + up) / 2)
            result['comp_num'] = comp_num
    # 目标值未找到，返回错误码
    result['address'] = -1
    return result


# 冒泡排序
# 算法特点：稳定算法
# 算法思路：每遍历一遍，都会把值最大的选择出来，并将列表中元素整理的局部有序
def bubblesort(l):
    index = len(l)
    i = 0
    # 外层循环-控制目前排序值的位置
    while i < index:
        j = i + 1
        # 内层循环-控制比较值的位置
        while j < index:
            if l[i] >= l[j]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
            j = j + 1
        i = i + 1
    return l


# 快速排序算法
# 算法特点：稳定算法，冒泡排序算法的改进
# 算法思路：选择一个比较值，将待排序列表整理成小值集合和大值集合，然后在小值集合和大值集合重复划分方法，直到每个划分仅存一个元素，排序结束
# 快速排序是现存已知效率最好，应用中出现最多的排序算法
def quicksort(down, uper, l):
    # 变量i控制划分自区间的遍历操作
    i = down + 1
    # 遍历m记录区间内小于划分值的位置
    m = down
    # 异常判断，待排序区间高低地址出错
    if down >= uper:
        return l
    # 初始化操作，在list中随机选择一个划分值
    swap(down, random.randint(down, uper), l)
    # 顺序遍历待排序列表，查找比划分值小的元素位置，并交换
    while i <= uper:
        if l[i] < l[down]:
            m = m + 1
            swap(m, i, l)
        i = i + 1
    # 将划分值与m交换位置，此时划分值左边是小值区间，右边是大值区间
    swap(down, m, l)
    # 递归调用本算法，继续进行小值区间和大值区间的快速排序算法，直至排序结束，程序返回
    quicksort(down, m - 1, l)
    quicksort(m + 1, uper, l)
    return l


# 交换列表元素方法
# 给方法传输待排序元素的地址，借助一个临时空间完成两个地址中元素值的交换操作
def swap(a, b, l):
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp
    return l


# 插入排序
# 算法特点：稳定算法，适应性算法
# 算法思路：每次选择无序序列中的一个元素，查找它在有序部分的插入点，插入目标元素，并向后移动有序部分的其他元素，直至列表中所有元素有序
def insertsort(l):
    # 申请一个遍历i，循环遍历要插入的元素
    i = 0
    for i in range(len(l)):
        # 将要插入的元素暂存在变量
        x = l[i]
        # 初始化插入点比较变量
        j = i
        # 当插入比较的位置大于0并且位置的值比要插入的值大时，将该位置元素后移
        # 当插入比较的值等于0或者位置的值比要插入的值小时，退出循环，找到了要插入元素的位置
        while j > 0 and l[j - 1] > x:
            l[j] = l[j - 1]
            j = j - 1
        # 将待插入元素插入找到的位置
        l[j] = x
    return l


# 选择排序
# 算法特点：稳定算法，适应性算法
# 算法思路：每次从待选序列中选择一个最小元素，然后插入到已排序部分的末尾，直至所有元素选择完毕，算法实践复杂度为o（n方）
def selectsort(l):
    # 遍历列表中所有元素，i表示当前待插入的最小元素位置
    for i in range(len(l)):
        k = i
        # 遍历未排序列表部分，找出最小元素的所在位置
        for j in range(i, len(l)):
            if l[j] < l[k]:
                k = j
        # 如果找到的最小元素不是当前位置元素，则将当前位置元素于搜索到的最小元素互换位置
        if k != i:
            tmp = l[i]
            l[i] = l[k]
            l[k] = tmp
    # 返回已排序好的列表
    return l


# 执行最基本的冒烟测试实例
if __name__ == '__main__':
    # 初始化测试用例
    mb = 6
    print('待查找的目标值为：%d' % mb)
    print('---------------------------')
    l = [1, 2, 3, -4, 5, 54, -27, 61, 102]
    # 输出原列表元素
    print('原列表为：%s' % l)
    # lsort = quicksort(0, 8, l)
    lsort = insertsort(l)
    print(lsort)
    # # 顺序查找
    # res_sequence = sequencesearch(l, mb)
    # print('经过%d次比较后，SequenceSearch,找到目标值在列表的位置为：%d' % (res_sequence['comp_num'], res_sequence['address']))
    # print('---------------------------')
    # # 列表排序，顺序排序【可以选择：冒泡排序、插入排序、选择排序三种算法】
    # lsort = selectsort(l)
    # # 输出排序后列表元素
    # print('顺序排序后的列表为：%s' % lsort)
    # # 折半查找
    # res_binary = binarysearchv3(lsort, mb)
    # # 差值查找
    # res_insert = insertsearch(lsort, mb)
    # # 查找结果集输出到控制台
    # # 查找位置等于000代表查找失败，查找位置不等于000代表查找成功
    # print('经过%d次比较后，BinarySearch,找到目标值在列表的位置为：%s' % (res_binary['comp_num'], res_binary['address']))
    # print('经过%d次比较后，InsertSearch,找到目标值在列表的位置为：%d' % (res_insert['comp_num'], res_insert['address']))
