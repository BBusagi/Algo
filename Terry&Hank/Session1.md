# Binary Search
特征 整个数字可以明显分为左右两边  
时间复杂度 Ologn  
难点1 l和r的变换之后的取值  
难点2 循环结束的条件，在最后一种情况之后  

# 153. Find Minimum in Rotated Sorted Array
一般对比是linear time  
左右两边呈现单调性 → binary reach Ologn

1. 先判断特殊case
2. 判断当不存在元素的时候
3. 【二分搜索】

### Test case
无元素 []
一个元素 [0]
两个元素 [1,0]
两个元素 [0,1]
整体单调 [0,1,2,3,4]
[3，4，0，1，2]
[2，3，4，0，1，2]
[2,3,4,0,1]

# Follow Up - 154. Find Minimum in Rotated Sorted Array II
原来为无重复，如果当允许重复呢？

[3,3,3,4,2]
[3,3,3,4,5,3]
[3,3,3,4,3,3]
Ologn + duplicateNumber

1. 先判断特殊case
2. 先处理数组，保证最后一个数和左边的第一个数不相等
2. 判断当不存在元素的时候
3. 【二分搜索】