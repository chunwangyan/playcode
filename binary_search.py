import math
import random


# 折半查找法【适用于各种有序列表类型】
# 算法特点：稳定，适用性较好
# 算法思路：待查找的集合必须是有序的向量存储集合，通过比较判定目标值的区间，逐步缩小查找范围，事件复杂度（O(logn)）
# 本算法的实现有一个bug,当数据足够到，超出类型的最大值时，程序会发生内存溢出【(down + up) / 2】
# 改进算法：(down + up) / 2 修改为 移位运算 (down + up) >> 1
def binarysearch(l, mb):
    m = mb
    # 查询列表低值索引
    down = 0
    # 查询列表高值索引
    up = len(l) - 1
    # 查询列表比较值索引
    mid = math.ceil((down + up) >> 1)
    # 记录查询比较次数
    comp_num = 0
    # 返回结果集
    result = {}
    if m < l[down] or m > l[up]:
        result['comp_num'] = 0
    # 边界判断，如果查找值超出查找范围，不比较，直接跳出循环
    while down <= up and m >= l[down] and m <= l[up]:
        # 目标值找到
        if m == l[mid]:
            comp_num += 1
            result['comp_num'] = comp_num
            result['address'] = mid
            return result
        # 目标值比当前比较值小，将高值索引前移至当前比较值
        elif m < l[mid]:
            comp_num += 1
            up = mid - 1
            # 结果值向上取整
            mid = math.ceil((down + up) >> 1)
            result['comp_num'] = comp_num
        # 目标值比当前比较值大，将低值索引后移至当前比较值
        else:
            comp_num += 1
            down = mid + 1
            mid = math.ceil((down + up) >> 1)
            result['comp_num'] = comp_num
    # 目标值未找到，返回错误码
    result['address'] = 999
    return result


# 顺序查找法
# 算法特点：不稳定，不要求查找列表有序，适用性最好
# 算法思路：遍历列表所有元素，查找与目标值相等的元素，不要求列表元素有序，不要求列表元素固定数据类型，算法事件复杂度（O(n)）
def sequencesearch(l, mb):
    m = mb
    # 记录比较次数
    comp_num = 0
    # 记录返回结果集
    result = {}
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
    result['address'] = 999
    return result


# 差值查找法【二分查找的改进型，适用于查找表值分布均匀,查找集合比较大
# 算法特点：不稳定，特殊情况下比二分查找效率高
# 算法思路：根据目标值在查找范围的分布区间取比较值，逐步缩小查找范围，以期减少查询比较次数
def insertsearch(l, mb):
    m = mb
    # 查询列表低值索引
    down = 0
    # 查询列表高值索引
    up = len(l) - 1
    # 查询列表比较值索引[索引点选择依据是查找值在查找区间的分布情况]
    if l[up] - l[down] > 0:
        mid = down + math.floor((m - l[down]) / (l[up] - l[down]) * (up - down))
    else:
        mid = math.ceil((down + up) / 2)
    # 记录查询比较次数
    comp_num = 0
    # 返回结果集
    result = {}
    if m < l[down] or m > l[up]:
        result['comp_num'] = 0
    # 边界判断，如果查找值超出查找范围，不比较，直接跳出循环
    while down <= up and m >= l[down] and m <= l[up]:
        # 目标值找到
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
    result['address'] = 999
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
            l[j - 1] = l[j]
            j = j - 1
        # 将待插入元素插入找到的位置
        l[j] = x
    return l


# 插入排序
# 算法特点：稳定算法，适应性算法
# 算法思路：每次从待选序列中选择一个最小元素，然后插入到已排序部分的末尾，直至所有元素选择完毕，算法实践复杂度为o（n方）
def selectsort(l):
    # 申请一个循环变量i
    i = 0
    # 遍历列表中所有元素，i表示当前待插入的最小元素位置
    for i in range(len(l)):
        k = i
        # 遍历未排序列表部分，找出最小元素的所在位置
        for j in range(i, len(l)):
            if l[j] < l[k]:
                k = j
        # 如果找到的最小元素不是当前位置元素，则将当前位置元素于搜索到的最小元素互换位置
        if k != i:
            tmp = l[i];
            l[i] = l[k]
            l[k] = tmp
    # 返回已排序好的列表
    return l


if __name__ == '__main__':
    # 初始化一个包含n个元素的列表
    n = 1000
    i = 0
    l = [16, 2, 3, 43, 5, 61, 1, 8, 9, 10]
    l2 = [16, 2, 3, 43, 5, 61, 1, 8, 9, 10]
    # while i <= n:
    #     l.append(random.randint(1, 100))
    #     i += 1
    #   lsort = bubblesort(l)
    lsort = selectsort(l)
    print(lsort)
    mb = 61
    # 折半查找
    res_binary = binarysearch(lsort, mb)
    # 顺序查找
    res_sequence = sequencesearch(l2, mb)
    # 差值查找
    res_insert = insertsearch(lsort, mb)
    # 查找结果集输出到控制台
    if res_binary['address'] != 999:
        print('经过%d次比较后，BinarySearch查找成功,找到目标值在列表的位置为：%d' % (res_binary['comp_num'], res_binary['address']))
        print('经过%d次比较后，SequenceSearch查找成功,找到目标值在列表的位置为：%d' % (res_sequence['comp_num'], res_sequence['address']))
        print('经过%d次比较后，InsertSearch查找成功,找到目标值在列表的位置为：%d' % (res_insert['comp_num'], res_insert['address']))
    else:
        print('经过%d次比较后，BinarySearch查找失败，目标值在列表中不存在！！' % res_binary['comp_num'])
        print('经过%d次比较后，SequenceSearch查找成功，目标值在列表中不存在！！' % res_sequence['comp_num'])
        print('经过%d次比较后，InsertSearch查找成功，目标值在列表中不存在！！' % res_insert['comp_num'])
