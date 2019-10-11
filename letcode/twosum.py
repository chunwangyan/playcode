class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j) and (target - nums[i] == nums[j]):
                    res.append(i)
                    res.append(j)
        return list(set(res))


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    nums = [2, 7, 3, 3, 11, 3, 15]
    target = 6
    res = Solution2()
    print(res.twoSum(nums, target))
