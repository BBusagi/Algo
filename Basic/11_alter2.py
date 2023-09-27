# 自己的方法 将数组从链表中取出
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def getList(self, headNode):
        lst = []
        curr = headNode
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst
    
    def mergeSort(self,arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]
        
        self.mergeSort(left)
        self.mergeSort(right)
        merged = self.merge(left, right)
        for i in range(len(merged)):
            arr[i] = merged[i]

        return arr

    def merge(self,left,right):
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

    #主要调用口
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = self.getList(head)
        return self.mergeSort(arr)
    
sol = Solution()
node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1


print(sol.getList(head))