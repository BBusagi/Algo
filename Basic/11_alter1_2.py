# 本脚本为根据1的方法，进行改进
# 包括两个改进点 #1 #2
class Solution(object):
    def mergeSort(self, arr):
        if len(arr) <= 1: return
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        self.mergeSort(left)
        self.mergeSort(right)
        self.merge_st(left, right,arr)

    #1. 利用arr数组直接修改arr
    def merge_st(self,left,right,arr):
        k = 0
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1            

    def merge(self, nums1, m, nums2, n):
        
        #2. 利用切片操作简化赋值
        nums1[m:m+n] = nums2

        self.mergeSort(nums1)


'''
算法复杂度不变
'''