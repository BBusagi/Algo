# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        left = head 

        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, nodes):
        slow, fast = nodes, nodes.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self,left,right): 
        res = tail= ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

            if left:
                tail.next = left
            if right:
                tail.next = right
        
        return res.next

sol = Solution()
node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
head = node1

print(sol.sortList(head))

'''
时间复杂度：O(n log n)
空间复杂度是：O(log n)
'''