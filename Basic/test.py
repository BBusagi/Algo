class Solution(object):
    def mergeSort(self, arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        self.mergeSort(left)
        self.mergeSort(right)
        new_arr = self.merge_st(left,right)

        return new_arr

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
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m,len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        if len(nums1) == 1:
            return nums1
        
        self.mergeSort(nums1)
