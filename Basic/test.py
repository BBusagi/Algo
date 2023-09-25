class ListNode:
    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

map = [ListNode() for i in range(3)]
print(map)
node1 = ListNode()
node2 = ListNode()

map[0].next = None

test_node = map[0].next

if test_node:
    print(test_node)
    print(11111)
else:
    print("None")