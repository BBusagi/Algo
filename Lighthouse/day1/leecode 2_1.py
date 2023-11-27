# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getnum(self, node):
        num = node.val
        n = 0
        while(node.next):
            node = node.next
            n += 1
            num += node.val * (10 ** n)            
        return num

    def creat_linked(self, list):
        if not list:
            return ListNode(0)
    
        dummy_head = ListNode(0)
        current = dummy_head
        for n in list:
            current.next = ListNode(n)
            current = current.next

        return dummy_head.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getnum(l1)
        num2 = self.getnum(l2)
        num3 = num1 + num2

        num3_str = str(num3)
        num3_list = []
        for n in num3_str:
            num3_list.append(n)
        num3_list.reverse()
        
        return self.creat_linked(num3_list)        