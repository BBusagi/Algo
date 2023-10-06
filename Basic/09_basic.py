class TreeNode:
    # 创建结点结构
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start  
        self.end = end  
        self.val = val  
        self.left = left  
        self.right = right  

# 创建片段树
def buildTree(start, end, vals):
    # 若为叶子结点，创建为基本数字结点
    if start == end:
        return TreeNode(start,end, vals[start])
    
    # 递归左右结点
    mid = (start + end) // 2
    left = buildTree(start, mid, vals)
    right = buildTree(mid + 1, end, vals)
    return TreeNode(start, end, left.val + right.val, left, right)

# 更新片段树指定结点
def updateTree(node:TreeNode, index, new_val):
    # 若更新到叶子结点，更新
    if node.start == node.end == index :
        node.val = new_val
        return
    
    # 根据索引决定是左还是右
    mid = (node.start + node.end) // 2
    if index <= mid:
        updateTree(node.left, index, new_val)
    else:
        updateTree(node.right, index, new_val)
    
    # 更新结点数值
    node.val = node.left.val + node.right.val
    return node.val

# 查询片段值
def querySum(root:TreeNode, i, j):
    # base case
    if root.start == i and root.end == j:
        return root.val
    
    mid = (root.start + root.end) // 2    # mid计算当前区间标准值
    # 三种情况
    if j <= mid:
        return querySum(root.left, i, j)
    elif i > mid:
        return querySum(root.right, i, j)
    else:
        return querySum(root.left, i, mid) + querySum(root.right, mid + 1, j)

vals = [1, 3, 5, 7, 9]
root = buildTree(0, len(vals)-1, vals)
updateTree(root, 2, 10)
result = querySum(root, 1, 3)
print(result)

'''
def1 O(N)
def2 O(log N)
def3 O(log N) - O(N)
'''