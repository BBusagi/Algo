class ListNode:
    def __init__(self, val, next, prev):
        self.val, self.next, self.prev = val, next, prev


class MyCircularQueue(object):

    def __init__(self, k):
        self.space = k
        self.left = ListNode(0,None,None) #dummy node
        self.right = ListNode(0,None,self.left) #dummy node
        self.left.next = self.right
        

    def enQueue(self, value):
        if self.isFull() :    return False
        curr = ListNode(value,self.right,self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.space -= 1
        return True

    def deQueue(self):
        if self.isEmpty(): return False
        #FILO
        # self.right.prev.prev.next = self.right
        # self.right.prev = self.right.prev.prev

        #FIFO
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        
        self.space += 1
        return True        

    def Front(self):
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self):
        return self.left.next == self.right
        
    def isFull(self):
        return self.space == 0