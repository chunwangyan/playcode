import math


# 折半查找法【适用于各种有序列表类型】
# 算法特点：稳定，适用性较好
# 算法思路：待查找的集合必须是有序的向量存储集合，通过比较判定目标值的区间，逐步缩小查找范围，事件复杂度（O(logn)）
def binarysearch(l, mb):
    m = mb
    # 查询列表低值索引
    down = 0
    # 查询列表高值索引
    up = len(l) - 1
    # 查询列表比较值索引
    mid = math.ceil((down + up) / 2)
    # 记录查询比较次数
    comp_num = 0
    # 返回结果集
    result = {}
    while down <= up:
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
            mid = math.ceil((down + up) / 2)
            result['comp_num'] = comp_num
        # 目标值比当前比较值大，将低值索引后移至当前比较值
        else:
            comp_num += 1
            down = mid + 1
            mid = math.ceil((down + up) / 2)
            result['comp_num'] = comp_num
    # 目标值未找到，返回错误码
    result['address'] = 999
    return result


# 顺序查找法
# 算法特点：不稳定，不要求查找列表有序，适用性最好
# 算法思路：遍历列表所有元素，查找与目标值想等的元素，不要求列表元素有序，不要求列表元素固定数据类型，算法事件复杂度（O(n)）
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
    mid = down + math.ceil((m - l[down]) / (l[up] - l[down]) * (up - down))
    # mid = math.ceil((down + up) / 2)
    # 记录查询比较次数
    comp_num = 0
    # 返回结果集
    result = {}
    while down <= up:
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
            mid = down + math.ceil((m - l[down]) / (l[up] - l[down]) * (up - down))
            result['comp_num'] = comp_num
        # 目标值比当前比较值大，将低值索引后移至当前比较值
        else:
            comp_num += 1
            down = mid + 1
            mid = down + math.ceil((m - l[down]) / (l[up] - l[down]) * (up - down))
            result['comp_num'] = comp_num
    # 目标值未找到，返回错误码
    result['address'] = 999
    return result


if __name__ == '__main__':
    # 情形一：查找列表值分布不均匀
    l = [1, 2, 3, 4, 5, 9, 172, 383, 1718, 6590, 100191]
    # 情形二：列表元素较多，分布较均匀
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 42, 53, 124, 225, 326, 627, 728,
          829, 930]
    mb = 18
    # 折半查找
    res_binary = binarysearch(l2, mb)
    # 顺序查找
    res_sequence = sequencesearch(l2, mb)
    # 差值查找
    res_insert = insertsearch(l2, mb)
    # 查找结果集输出到控制台
    if res_binary['address'] != 999:
        print('经过%d次比较后，BinarySearch查找成功,找到目标值在列表的位置为：%d' % (res_binary['comp_num'], res_binary['address']))
        print('经过%d次比较后，SequenceSearch查找成功,找到目标值在列表的位置为：%d' % (res_sequence['comp_num'], res_sequence['address']))
        print('经过%d次比较后，InsertSearch查找成功,找到目标值在列表的位置为：%d' % (res_insert['comp_num'], res_insert['address']))
    else:
        print('经过%d次比较后，BinarySearch查找失败，目标值在列表中不存在！！' % res_binary['comp_num'])
        print('经过%d次比较后，SequenceSearch查找成功，目标值在列表中不存在！！' % res_sequence['comp_num'])
        print('经过%d次比较后，InsertSearch查找成功，目标值在列表中不存在！！' % res_insert['comp_num'])
