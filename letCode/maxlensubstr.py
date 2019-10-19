class Solution:
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


def alluniq(str):
    sets = set()
    for i in str:
        sets.add(i)
    if len(str) == len(sets):
        return 1
    else:
        return 0


if __name__ == '__main__':
    obj = Solution()
    str = "aaaaabcfrt"
    substr = obj.cut(str)
    print(obj.lengthOfLongestSubstring(substr))
    # print(alluniq(str))
