def isTure(sublist, berthsaturation):
    flag = 0
    for i in sublist:
        if berthsaturation[i] < 0.8:
            flag = flag + 1
    if len(sublist) >= 3 and flag == 0:
        return 1
    else:
        return 0


# 判断列表元素是否都大于0.8
def isTure_v2(slist):
    i = len(slist) - 1
    while i >= 0:
        if slist[i] < 0.8:
            return 0
        else:
            i = i - 1
    return 1


# 暴力识别算法
class Solution:
    def lengthOfLongestSubstring(self, list, berthsaturation):
        res = []
        for i in list:
            if isTure(i, berthsaturation) == 1:
                res.append(i)
        return res

    def cut(self, list):
        results = []
        # x + 1 表示子字符串长度
        for x in range(len(list)):
            # i 表示偏移量
            for i in range(len(list) - x):
                results.append(list[i:i + x + 1])
        return results


def filter(subduration):
    tmp = []
    for i in subduration:
        for j in subduration:
            if i != j and (set(i) < set(j)):
                tmp.append(i)
    res = [k for k in subduration if k not in tmp]
    return res


# 滑动窗口算法2
class Solution_v2:
    def parkingdurationanalysis(self, list):
        # i控制窗口起始位置，j控制窗口结束位置
        i = 0
        listlen = len(list)
        j = listlen
        res = []
        while i < len(list) and j >= i:
            if list[i] < 0.8:
                i = i + 1
            elif isTure_v2(list[i:j]) == 0:
                j = j - 1
            else:
                if len(list[i:j]) >= 3:
                    # print(list[i:j])
                    res.append(list[i:j])
                i = i + 1
                j = listlen
        return res


# 滑动窗口算法3
class Solution_v3:
    def parkingdurationanalysis_v3(self, list):
        # i控制窗口起始位置，j控制窗口结束位置
        i = 0
        j = i
        # listlen表示列表最大长度
        listlen = len(list)
        # res存储返回值
        res = []
        # 阀值
        threshold = 0.7
        # 子列表长度
        sublistlen = 3
        # 当窗口的起始和结束位置都在目标列表范围内时，条件满足
        while i < listlen and j >= i and j < listlen:
            # 判断起始位置元素是否满足大于0.8饱和度，不满足则将窗口位置后移
            if list[i] < threshold:
                i = i + 1
                j = i
            # 找到一个满足条件的子列表
            elif list[j] < threshold and j - i >= sublistlen:
                res.append(list[i:j])
                i = j
                j = i
            # 如果找到的字串，起始位置满足要求，结束位置不满足要求，窗口后移
            elif list[j] < threshold and j - i < sublistlen:
                i = j + 1
                j = i
            # 滑动窗口起始位置不变，结束位置后移
            else:
                j = j + 1
        # 返回找到的所有满足条件的子列表
        return res


if __name__ == '__main__':
    # index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    #          11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    #          21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    #          31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    #          41, 42, 43, 44, 45, 46]
    berthsaturation = [0.5, 0.4, 0.8, 0.9, 0.95, 0.5, 0.4, 0.3, 0.2, 0.1,
                       0.8, 0.1, 0.9, 0.8, 0.5, 0.3, 0.2, 0.1, 0.4, 0.5,
                       0.8, 0.9, 0.1, 0.3, 0.6, 0.5, 0.7, 0.98, 0.76, 0.1,
                       0.1, 0.8, 0.98, 0.98, 0.87, 0.2, 0.3, 0, 3, 0.2, 0.1,
                       0.1, 0.85, 0.9, 0.8, 0.2, 0.3, 0.4]
    # duration = Solution()
    # subduration = duration.cut(index)
    # maxlen = duration.lengthOfLongestSubstring(subduration, berthsaturation)
    # result = duration.filter(maxlen)
    # print(result)
    # print(maxlen)
    # qujian = duration.filter(maxlen)
    # print(qujian)

    # res = Solution_v2()
    # list = res.parkingdurationanalysis(berthsaturation)
    # print(filter(list))

    res = Solution_v3()
    list = res.parkingdurationanalysis_v3(berthsaturation)
    print(list)
