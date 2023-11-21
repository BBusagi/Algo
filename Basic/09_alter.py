from typing import List

class TreeNode:
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start  
        self.end = end  
        self.val = val  
        self.left = left  
        self.right = right  

class NumArray:
    def __init__(self, nums: List[int]):

        def buildTree(start, end, vals):
            if start == end:
                return TreeNode(start, end, vals[start])
            
            mid = (start + end) // 2
            left = buildTree(start, mid, vals)
            right = buildTree(mid + 1, end, vals)
            return TreeNode(start, end, left.val + right.val, left, right)
        
        self.root = buildTree(0, len(nums)-1, nums)

    def update(self, index: int, val: int) -> None:
        def updateTree(node, index, new_val):
            if node.start == node.end == index:
                node.val = new_val
                return
            mid = (node.start + node.end) // 2
            if index <= mid:
                updateTree(node.left, index, new_val)
            else:
                updateTree(node.right, index, new_val)
            node.val = node.left.val + node.right.val

        updateTree(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def querySum(root, i, j):
            if root.start == i and root.end == j:
                return root.val
            mid = (root.start + root.end) // 2
            if j <= mid:
                return querySum(root.left, i, j)
            elif i > mid:
                return querySum(root.right, i, j)
            else:
                return querySum(root.left, i, mid) + querySum(root.right, mid + 1, j)

        return querySum(self.root, left, right)

# 示例：
nums = [1, 3, 5, 7, 9]
obj = NumArray(nums)
print(obj.sumRange(1, 3))  # 输出: 15
obj.update(2, 10)
print(obj.sumRange(1, 3))  # 输出: 20
