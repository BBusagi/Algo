class ListNode:
    # Chaining node
    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap(object):

    length = int()
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        self.length = len(self.map)

    def hash(self,key):
        return key % self.length

    def put(self, key, value):
        curr = self.map[self.hash(key)]
        # if not exist
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
    
        # if not exist
        curr.next = ListNode(key,value)

    def get(self, key):
        curr = self.map[self.hash(key)].next
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key):
        curr = self.map[self.hash(key)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# 自己的理解方法
    def remove2(self, key):
        prev = self.map[self.hash(key)]
        curr = prev.next

        while curr:
            if curr.key == key:
                if curr.next == None:
                    prev.next =None
                else:
                    prev.next = prev.next.next

            prev = prev.next
            curr = curr.next