def isTure(sublist, berthsaturation):
    flag = 0
    for i in sublist:
        if berthsaturation[i] < 0.8:
            flag = flag + 1
    if len(sublist) >= 3 and flag == 0:
        return 1
    else:
        return 0


class Solution:
    # 暴力识别算法
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

    def filter(self, subduration):
        tmp = []
        for i in subduration:
            for j in subduration:
                if i != j and (set(i) < set(j)):
                    tmp.append(i)
        res = [k for k in subduration if k not in tmp]
        return res


if __name__ == '__main__':
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
             41, 42, 43, 44, 45, 46]
    berthsaturation = [0.5, 0.4, 0.8, 0.9, 0.95, 0.5, 0.4, 0.3, 0.2, 0.1,
                       0.8, 0.1, 0.9, 0.8, 0.5, 0.3, 0.2, 0.1, 0.4, 0.5,
                       0.8, 0.9, 0.1, 0.3, 0.6, 0.5, 0.7, 0.98, 0.56, 0.1,
                       0.1, 0.8, 0.98, 0.98, 0.87, 0.2, 0.3, 0, 3, 0.2, 0.1,
                       0.1, 0.85, 0.9, 0.8, 0.2, 0.3, 0.4]
    duration = Solution()
    subduration = duration.cut(index)
    maxlen = duration.lengthOfLongestSubstring(subduration, berthsaturation)
    result = duration.filter(maxlen)
    print(result)
    # print(maxlen)
    # qujian = duration.filter(maxlen)
    # print(qujian)
