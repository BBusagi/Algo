# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    '''
    每次返回 1+max
    '''
    
    # BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        lvl = 0
        q = deque([root])
        while(q):
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl += 1
        return lvl
    '''
    每次保存父结点
    '''
    
    #iterative dfs
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        res = 1
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res,depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    '''
    栈结构存储为未处理结点
    '''