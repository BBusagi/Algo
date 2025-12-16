## TODO


## 统计



## 模板
+ 问题抽象 这是一个什么类型的问题
+ 问题重点 问题的难点在哪里
+ 有哪些解决方法？
+ 复杂度分析和优化

## 二叉树基本例题
+ [Easy] 94. Binary Tree Inorder Traversal --- 中序递归遍历
+ [Easy] 144. Binary Tree Preorder Traversal --- 前序递归遍历
+ [Easy] 145. Binary Tree Postorder Traversal --- 后序递归遍历
***---> 不用递归如何实现？***
+ [Medium] 102. Binary Tree Level Order Traversal --- 带有层级flag的层序遍历


## Easy
### [Easy] 2. Add Two Numbers
### [Easy] 9. Palindrome Number
### [Easy] 13. Roman to Integer
### [Easy] 66. Plus One



### [Easy] 766. Toeplitz Matrix
+ 重点 设想一下正确情况下会是怎么样
+ 解1 (i,j) (i+1,j+1)

### [Easy] 1295. Find Numbers with Even Number of Digits
+ 重点 如何获得位数
+ 解1 ToString().Length
+ 解2 Log10(n)+1获得位数

### [Easy] 1394. Find Lucky Integer in an Array
+ 重点 
+ 解1 字典Dictionary
+ 解2 数组，比字典更快

### [Easy] 1450. Number of Students Doing Homework at a Given Time
+ 重点 如何判断所在的范围

### [Easy] 1470. Shuffle the Array
+ 重点 如何分段
+ 解1 利用2n计算对位
+ 解2 linq直接获取前半段和后半段

### [Easy] 1480. Running Sum of 1d Array
+ 重点 数列，循环

### [Easy] 1952. Three Divisors
+ 重点 根号的数学定义
+ 解1 暴力枚举
+ 解2 根号的数学定义

### [Easy] 3024. Type of Triangle
+ 重点 两边之和大于第三边
+ 解1 暴力条件
+ 解2 先排序，时间稍受影响
+ 解3 max函数

### [Easy] 3028. Ant on the Boundary
+ 重点 循环

### [Easy] 3099. Harshad Number
+ 重点 位数之和
+ 解1 取位数
+ 解2 ToString()




## Medium
### [Medium] 424. Longest Repeating Character Replacement

### [Medium] 954. Array of Doubled Pairs 待优化
+ 重点 匹配消除
+ 解1 绝对值排序，hash匹配

### [Medium] 1004. Max Consecutive Ones III
+ 重点 
+ 解1 sliding window，外层为r的循环，内部携带0的个数n → On 
+ 解2 前缀和？


### [Medium] 1390. Four Divisors 待优化
+ 重点 如何获得因数
+ 解1 从开始，考虑短的一边 → O(n√m)，n = nums.Length m = max(nums)

### [Medium] 1482. Minimum Number of Days to Make m Bouquets 待优化
+ 重点 二分搜索
+ 解1 二分搜索，简化为bool[]，不断压缩为true的空间 → Onlogn

### [Medium]
### [Medium]


## LeeCode Contest
### weekly contest 468

### Weekly Contest 324

### [Contest] Biweekly Contest 97
#### Q1. Separate the Digits in an Array 可优化
重点 位数计算

#### Q2. Maximum Number of Integers to Choose From a Range I 可优化
重点 先获得有效数组

#### Q3. Maximize Win From Two Segments
+ 解1 双sliding window，固定一边后穷举另一边
+ 注意：greedy会错

#### Q4. Disconnect Path in a Binary Matrix by at Most One Flip
+ 重点 从上往下找 再从下往上找，然后确保只有一条有效路径
+ 解1
### 

### [Contest] Biweekly Contest 114
#### Q1. Minimum Operations to Collect Elements
+ 解 从后往前，转化为hashtable或者bool[]

#### Q2. Minimum Number of Operations to Make Array Empty
+ 解 hashtable

#### Q3. Split Array Into Maximum Number of Subarrays
+ 重点 确保globaland为最小，确保段数最多，转移函数？

####


## Tips
+ 简化题目
+ 思考 test case
+ 思考 follow up

+ 完全平方根 可以看作乘法的中位数
+ 可以直接将int转化为string = char[]
+ log10(n)+1 可以获得n的位数
+ 0 - 10^9 二分
+ 空间复杂度默认为O1

## 常用方法
+ 快速建立hashtable
```
var dic = new Dictionary<int, int>();
foreach (var n in nums)
    dic[n] = dic.GetValueOrDefault(n, 0) + 1;
```