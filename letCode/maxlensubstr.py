def alluniq(str):
    sets = set()
    for i in str:
        sets.add(i)
    if len(str) == len(sets):
        return 1
    else:
        return 0

class Solution:
    # 暴力识别算法
    def lengthOfLongestSubstring(self, list):
        maxlen = 0
        for i in list:
            if alluniq(i) == 1:
                tmp = len(i)
                if tmp > maxlen:
                    maxlen = tmp
        return maxlen

    def cut(self, str):
        results = []
        # x + 1 表示子字符串长度
        for x in range(len(str)):
            # i 表示偏移量
            for i in range(len(str) - x):
                results.append(str[i:i + x + 1])
        return results

    # 滑动窗口识别算法
    def lengthOfLongestSubstringv2(self, str):
        i = 0
        j = 0
        res = 0
        substr = set()
        while i < len(str) and j < len(str):
            if substr.__contains__(str[j]) == False:
                substr.add(str[j])
                j = j + 1
                if j - i > res:
                    res = j - i
            else:
                substr.remove(str[i])
                i = i + 1
        return res


if __name__ == '__main__':
    str = "abcabcabc"

    # 第一种解法：暴力识别
    # 先找出源字符串的所有子字符串，然后逐个判断字符是否重复，算出最长的不重复字串长度
    obj01 = Solution()
    substr_list = obj01.cut(str)
    res01 = obj01.lengthOfLongestSubstring(substr_list)
    print('暴力识别算法：', res01)
    print('---------------------')
    # 第二种解法：滑动窗口
    obj02 = Solution()
    res02 = obj02.lengthOfLongestSubstringv2(str)
    print('滑动窗口算法：', res02)
