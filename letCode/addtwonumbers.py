# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# 解决思路就是模拟整数加法的过程

#
# 测试用例	说明
# l1=[0,1]l1=[0,1]，l2=[0,1,2]l2=[0,1,2]	当一个列表比另一个列表长时
# l1=[]l1=[]，l2=[0,1]l2=[0,1]	当一个列表为空时，即出现空列表
# l1=[9,9]l1=[9,9]，l2=[1]l2=[1]	求和运算最后可能出现额外的进位，这一点很容易被遗忘


class solution(object):
    def addTwoNumbers(self, l1, l2):
        # 如果两个值中有一个为0，则直接返回另一个整数
        if len(l1) == 0 or l1[0] == 0:
            return l2
        if len(l2) == 0 or l2[0] == 0:
            return l1
        # 如果两个整数位数不同，较小者最高位补0
        if (len(l1) > len(l2)):
            for i in range(len(l1) - len(l2)):
                l2.append(0)
        if (len(l1) < len(l2)):
            for i in range(len(l2) - len(l1)):
                l1.append(0)
        # 存储加和进位标志
        flag = {}
        flag[-1] = 0
        # 存储返回结果
        res = []
        # 链表遍历
        for i in range(len(l1)):
            if l1[i] + l2[i] + flag[i - 1] < 10:
                flag[i] = 0
                res.append(l1[i] + l2[i] + flag[i - 1])
            if l1[i] + l2[i] + flag[i - 1] == 10:
                flag[i] = 1
                res.append(0)
            # 如果同位置数值之和大于10，标志位置1，结果取两个数的余数
            if l1[i] + l2[i] + flag[i - 1] > 10:
                flag[i] = 1
                res.append((l1[i] + l2[i] + flag[i - 1]) % 10)
        # 判断结果最后一位是否进位
        if flag[i] == 1:
            res.append(1)
            return res
        return res


if __name__ == '__main__':
    l1 = [1, 6, 3, 9]
    l2 = [2, 5, 9, 2, 3, 7, 9, 9]
    res = solution()
    print(res.addTwoNumbers(l1, l2))
