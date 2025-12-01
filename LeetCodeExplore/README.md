# LeetCode Explore [C#]
Top Interview Questions  
[Easy Collection](https://leetcode.com/explore/interview/card/top-interview-questions-easy/)
11 8 6 5 2 4 2 4 6

## Array
+ HashSet - 不需要重复  
  `<int> seen = new HashSet<int>();`  
+ Dictionary  
  `Dictionary<int, int> dict = new Dictionary<int, int>();`  

### E1
+ HashSet -要求inplace X
+ 双指针

### E2
+ 差值列表
```csharp
public class Solution {
    public int MaxProfit(int[] prices) {
        //计算差值列表
        int[] profits = new int[prices.Length - 1];
        int maxprofit = 0;
        for(int i = prices.Length-1 ; i > 0; i--)
        {
            var profit = prices[i] - prices[i - 1];
            if(profit > 0)
            {
                //将列表中大于0的进行相加
                maxprofit += profit;
            }
        }
        return maxprofit;
    }
}
```

### E3
+ 普通循环 - 超时 X
+ 直接计算最后的位置
+ 数组列表的拼接与剪裁 ?
+ -> follow up TODO, 3种方法 O(1)

### E4
+ HashSet
```csharp
public class Solution {
    public bool ContainsDuplicate(int[] nums) 
    {
        HashSet<int> seen = new HashSet<int>();
        //遍历数组
        foreach(var num in nums)
        {
            if(seen.Contains(num))
            {
                //如果在hashset中存在就返回true
                return true;
            }
            else
            {
                seen.Add(num);
            }
        }
        return false;
    }
}
```
+ LinQ.Distinct()  
  `return nums.Length != nums.Distinct().Count();`

### E5
+ HashSet
```csharp
public class Solution {
    public int SingleNumber(int[] nums) {
        //利用hashset的唯一性
        HashSet<int> seen = new HashSet<int>();
        foreach(var num in nums)
        {
            //当存在的时候，删除，不存在的时候，加入，直到最后只剩一个
            if(seen.Contains(num))
            {
                seen.Remove(num);
            }    
            else
            {
                seen.Add(num);
            }
        }
        return seen.First();
    }
}
```
+ TODO Bitwise XOR 

### E6 Intersection of Two Arrays II
+ HashSet - 重复的时候无法存储 X
+ 字典 计算出现次数
```csharp
public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        //将nums1 转化为 字典
        Dictionary<int, int> dict = new Dictionary<int, int>();
        foreach(var num in nums1)
        {
            if(dict.ContainsKey(num))
            {
                dict[num] ++;
            }
            else
            {
                dict[num] = 1;
            }
        }
        //检查num2在字典中的表现
        var result = new List<int>();
        foreach(var num in nums2)
        {
            if(dict.ContainsKey(num) && dict[num] > 0)
            {
                dict[num] --;
                result.Add(num);
            }
        }
        return result.ToArray();        
    }
}
```
+ -> follow up TODO

### E7
+ 数组与数字互换 - int long BigInteger
```csharp
public class Solution {
    public int[] PlusOne(int[] digits) {
        //超大int存储类型 BigInteger
        BigInteger num = BigInteger.Parse(string.Join("", digits));
        num++;
        return num.ToString().Select(n => n -'0').ToArray();
    }
}
```
+ LinQ.Aggregate();  
`BigInteger bigNum = digits.Aggregate(BigInteger.Zero, (acc, d) => acc * 10 + d);`
+ TODO 手动修改数组中的每一位

### E8
+ Array.Copy(newArray, nums, nums.Length);
+ 双指针  
+ -> follow up TODO

### E9
+ 暴力解法 O(n²)  
+ -> follow up: Dictionary

## String

### E1 
+ 元组交换 (arr[i], arr[j]) = (arr[j], arr[i]);



[Medium Collection](https://leetcode.com/explore/interview/card/top-interview-questions-medium/)
8 3 7 5 9 4 4 7 5

指令创建项目文件
dotnet new console -o MyAlgorithmProject
code .

dotnet new console -o EasyArray1


#部分核心概念
+ 排序的本质是减少逆数对
+ 查找的本质是减少搜索范围，提高查找效率。
+ dict[s[i]] = 1 VS dict.Add(key, value)
  + dict.Add(key, value) 不允许重复键对
  + dict[s[i]] = 1 已存在会自动更新