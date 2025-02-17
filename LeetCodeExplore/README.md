LeetCode Explore
Top Interview Questions  
[Easy Collection](https://leetcode.com/explore/interview/card/top-interview-questions-easy/)
11 8 6 5 2 4 2 4 6

## Array
+ HashSet 不需要重复

### E1
+ HashSet<int> seen = new HashSet<int>();

### E2
+ 差值列表

### E3
+ 普通循环 - 超时 X
+ 直接计算最后的位置
+ 数组列表的拼接与剪裁 ?
-> follow up TODO, 3种方法 O(1)

### E4
+ HashSet<int> seen = new HashSet<int>();
+ LinQ return nums.Length != nums.Distinct().Count();

### E5
+ HashSet
+ TODO Bitwise XOR 

### E6 Intersection of Two Arrays II
+ HashSet - 重复的时候无法存储 X
+ TODO 字典 计算出现次数？
-> follow up TODO

### E7
+ 数组与数字互换 int long BigInteger
+ TODO 手动修改数组中的每一位

### E8
+ Array.Copy(newArray, nums, nums.Length);
+ 双指针
-> follow up TODO

[Medium Collection](https://leetcode.com/explore/interview/card/top-interview-questions-medium/)
8 3 7 5 9 4 4 7 5

指令创建项目文件
dotnet new console -o MyAlgorithmProject
code .

dotnet new console -o EasyArray1


#部分核心概念
+ 排序的本质是减少逆数对
+ 查找的本质是减少搜索范围，提高查找效率。