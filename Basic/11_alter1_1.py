# 本脚本为自己的方法，直接修改mergesort
class Solution(object):
    def mergeSort(self, arr):
        if len(arr) <= 1: return
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        self.mergeSort(left)
        self.mergeSort(right)
        merged = self.merge_st(left, right)
        for i in range(len(merged)):
            arr[i] = merged[i]

    def merge_st(self,left,right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < len(left):
            res.append(left[i])
            i += 1
        
        while j < len(right):
            res.append(right[j])
            j += 1
        
        return res
            

    def merge(self, nums1, m, nums2, n):
        j = 0
        for i in range(m,m+n):
            nums1[i] = nums2[j]
            j += 1

        self.mergeSort(nums1)


'''
时间复杂度:O((m+n)log(m+n))
空间复杂度: O(m+n)

总的时间复杂度是由 merge 决定的，
因为它封装了整个操作并在其中调用了 mergeSort
而mergesort的复杂度为O(nlogn)
'''