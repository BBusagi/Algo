class ListNode:
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
