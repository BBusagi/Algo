# 本脚本为自己的方法，直接修改mergesort
class Solution(object):
    def mergeSort(self, arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        self.mergeSort(left)
        self.mergeSort(right)
        merged = self.merge_st(left, right)
        for i in range(len(merged)):
            arr[i] = merged[i]

        return merged

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
        for i in range(m,len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        if len(nums1) == 1:
            return nums1
        
        self.mergeSort(nums1)
