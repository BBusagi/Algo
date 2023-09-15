'''
题目：
爬楼梯(Easy)

描述：
假设你正在爬楼梯，需要 n 步才能到达顶部。每次你可以爬 1 或 2 个台阶。问：你有多少种不同的方法可以爬到楼顶？

示例：
输入：n=2       输出：2
解释：有两种方法可以爬到楼顶。
1 步 + 1 步
2 步

输入：n=3       输出：3
解释：有三种方法可以爬到楼顶。

1 步 + 1 步 + 1 步
1 步 + 2 步
2 步 + 1 步

要求：
请使用动态规划的方法解决这个问题。
尝试分析时间复杂度和空间复杂度。

考察点：动态规划 状态转移 边界条件
'''

#1 动态规划
def def1(n):
    dp =[None]* (n+1)
    dp[0] = 1
    dp[1] = 1

    for n in range(2,n+1):
        dp[n] = dp[n-1] + dp[n-2]
    
    return dp[n]
'''
时间复杂度：O(n)
空间复杂度：O(n)
评分：9/10
'''

#2 非记忆递归
def def2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return def2(n-1) + def2(n-2)
'''
时间复杂度：O(2^n)
空间复杂度：O(n)
评分：3/10
'''

#3 记忆化递归
def def3(n, rec):    
    if rec[n] is not None:
        return rec[n]
    
    if n == 0 or n == 1:
        rec[n] = 1
        return 1
    
    rec[n] = def3(n-1,rec) + def3(n-2,rec)
    return rec[n]
'''
时间复杂度：O(n)
空间复杂度：O(n)
评分：8/10
'''

def def3_chatGPT(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1
    memo[n] = def3_chatGPT(n-1, memo) + def3_chatGPT(n-2, memo)
    return memo[n]

# main()
input1= int(input())
#result = def3(input1)

rec = [None] * (input1 + 1)
result = def3(input1,rec)
print(rec)
print(result)