def generateParenthesis(n: int):
    result = []
    if n == 0:
        return result
    callBack("", 0, 0, n, result)
    return result

def callBack(s, left, right, n, result):
    if len(s) == 2*n:
        result.append(s)
        return
    
    if left < n:
        callBack(s + "(", left + 1, right, n, result)

    if right < left:
        callBack(s + ")", left, right + 1, n, result)

for i in range(10):
    output = generateParenthesis(i)
    print(len(output))

'''
卡塔兰数（Catalan numbers）
组合数学问题
1. 计算有效的括号组合的数量（就像您之前的问题）。
2. 计算不同的二叉树结构的数量。
3. 计算在多边形中划分为三角形的方法数。
'''