import math


# 折半查找法
# 折半查找算法实现
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


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    mb = 3
    # 折半查找
    res_binary = binarysearch(l, mb)
    # 顺序查找
    res_sequence = sequencesearch(l, mb)
    # 查找结果集输出到控制台
    if res_binary['address'] != 999:
        print('经过%d次比较后，BinarySearch查找成功,找到目标值在列表的位置为：%d' % (res_binary['comp_num'], res_binary['address']))
        print('经过%d次比较后，SequenceSearch查找成功,找到目标值在列表的位置为：%d' % (res_sequence['comp_num'], res_sequence['address']))
    else:
        print('经过%d次比较后，BinarySearch查找失败，目标值在列表中不存在！！' % res_binary['comp_num'])
        print('经过%d次比较后，SequenceSearch查找成功，目标值在列表中不存在！！' % res_sequence['comp_num'])
