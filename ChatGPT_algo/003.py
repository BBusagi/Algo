'''
题目：合并两个有序数组
描述：
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

注意:

初始，nums1 和 nums2 的元素数量分别是 m 和 n。
你可以假设 nums1 有足够的空间（数组长度大于或等于 m + n）来保存来自 nums2 的额外元素。

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

输入：
nums1: 有序整数数组，长度为 m+n，其中前 m 个元素代表有效元素。
m: nums1 的有效元素数量。
nums2: 有序整数数组，长度为 n。
n: nums2 的元素数量。

输出：
无输出。在原数组 nums1 上直接进行修改。

示例：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3
merge(nums1, m, nums2, n)
# 输出: nums1 应为 [1,2,2,3,5,6]
'''

from typing import List

#1 自己的方法
def merge1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for n in nums2:
        print(n)
        nums1.append(n)

    nums1.sort()
    print(nums1)

#1_1 非全局排序 
def merge1_1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    point = 0
    for j in range(n):                          # n次
        changed = False
        for i in range(m + point):              # point与n有关，所以最坏情况(m+n)次
            if nums2[j] < nums1[i]:
                nums1.insert(i,nums2[j])
                point += 1
                changed = True
                break
        if not changed:
            nums1.append(nums2[j])

    print(nums1)

'''
时间复杂度 O((m + n) * m)
空间复杂度 O(1)
'''

#1_2 非重新分配空间
#TODO

# main()
# input1 = input("数组1：")
# input1_1 = input("有效数字：")
# input2 = input("数组2：")
# input2_1 = input("有效数字：")

# test1
input1 = "1,2,4,7"
input1_1 = "4"
input2 = "3,6,8"
input2_1 = "3"

# #test2
# input1 = "3,46,79,81"
# input1_1 = "4"
# input2 = "46,57,91"
# input2_1 = "3"

nums1 = list(map(int,input1.split(",")))
m = int(input1_1)
nums2 = list(map(int,input2.split(",")))
n = int(input2_1)

merge1_1(nums1,m,nums2,n)