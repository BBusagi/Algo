'''
题目：两数之和 (Easy)
描述：
给定一个整数数组 nums 和一个目标值 target，请你找出数组中和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例：
输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为 nums[0] + nums[1] = 2 + 7 = 9，所以返回 [0, 1]。

要求：
尝试使用不同的方法来解决这个问题，例如使用哈希表。

考察点：数组操作，哈希表
'''

#1 自己的方法_双指针
def def1 ():
    nums = input("数组")
    target = input("目标数值")
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))
    result=[]
    #print(nums_list) checkpoint
    find = False

    for left in range(0,len(nums_list)):
        for right in range(len(nums_list)-1,-1,-1):
                if left == right : continue
                num_sum = nums_list[left] + nums_list[right]
                #print(left," ",right," ",num_sum) checkpoint

                if num_sum == target_int:
                    #print("find") checkpoint
                    result[0],result[1] = left,right
                    find = True
                    break
                else:
                    result = [-1, -1]
        if find : break
    print(result)
'''
时间复杂度 O(n^2)

评分：
功能完整性：7/10（基本实现了功能，但有一些小错误和不必要的代码）
代码质量：5/10（有一些不符合最佳实践的地方）
算法效率：4/10（使用了O(n^2)的暴力解法，而更高效的解法是可用的）
总评分：16/30
'''

#1_1 优化
def def1_1 (nums,target):       #函数参数传递
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))
    result=[-1,-1]              #初始化为默认结果，减少后期
    find = False

    for left in range(0,len(nums_list)):
        for right in range(len(nums_list)-1,-1,-1):
                if left == right : continue
                num_sum = nums_list[left] + nums_list[right]

                if num_sum == target_int:
                    result[0],result[1] = left,right
                    find = True
                    break

        if find : break

    return result               #return输出结果
'''
评分：
功能完整性：9/10
代码质量：8/10
算法效率：4/10（题目规模较小的情况下可能是可接受的）
'''

#2 排序双指针
def def2 (nums,target):
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))
    nums_sorted = sorted(nums_list)
    print(nums_sorted)
    
    left, right = 0, len(nums_sorted) - 1
    result=[-1,-1]

    while left < right:
        num_sum = nums_sorted[left] + nums_sorted[right]
        if num_sum == target_int:
            result[0] =nums_list.index(nums_sorted[left])
            result[1] =nums_list.index(nums_sorted[right])
            return result
        elif num_sum < target_int:
            left +=1
        elif num_sum > target_int:
            right -=1
'''
评分：
正确性：8/10（代码能解决问题，但没有处理重复元素的情况）
可读性：8/10（代码结构清晰，但缺少注释）
效率：8/10（使用了排序，时间复杂度为O(nlogn)，但空间复杂度也相对较高）
-> 重复元素问题，且不修改原始数据
'''

#2_1 排序双指针_改进
def def2_1 (nums,target):
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))
    nums_sorted = sorted(nums_list)
    print(nums_sorted)
    
    left, right = 0, len(nums_sorted) - 1
    result=[-1,-1]

    while left < right:
        num_sum = nums_sorted[left] + nums_sorted[right]
        if num_sum == target_int:
            result[0] =nums_list.index(nums_sorted[left])
            if nums_sorted[left] == nums_sorted[right]:         #解决重复问题
                 temp = nums_list[result[0]]
                 nums_list[result[0]] = None                    #将第一次出现设置为none
                 changed = True                                 #记录是否更改原数据
            result[1] =nums_list.index(nums_sorted[right])
            if changed:                                         #恢复原数据
                 nums_list[result[0]] = temp
            return result
        elif num_sum < target_int:
            left +=1
        elif num_sum > target_int:
            right -=1
'''
评分：
正确性：10/10（代码能解决问题，包括处理重复元素）
可读性：8/10（代码结构清晰，但缺少注释）
效率：8/10（使用了排序，时间复杂度为O(nlogn)，但空间复杂度也相对较高）

关于注释：
更多的注释通常会更有帮助。例如：
1.在函数开始处，简要描述函数的作用、输入和输出。
2.在关键变量（如 left, right, result 等）旁边添加注释，解释它们的作用。
3.在逻辑复杂或不直观的代码段旁边添加注释。

关于空间复杂度：
nums_sorted，创建新的排序数组，会占用额外的 O(n) 空间 + 几个额外常数空间需求
总体空间复杂度是 O(n)
但如果输入数组非常大，可能会成为问题。
'''

#3 暴力解法
def def3(nums,target):
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))

    for i in range(len(nums_list)):
        for j in range(i+1,len(nums_list)):
            num_sum = nums_list[i] + nums_list[j]
            if num_sum == target_int:
                return [i,j]
    
    return[-1,-1]
'''
时间复杂度 O(n^2)
空间复杂度 O(1)
'''

#4 哈希表
def def4(nums,target):
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))
    hashtable = {}

    for num in nums_list:
        i = nums_list.index(num)
        complement = target_int - num
        if complement in hashtable:
            return [i,hashtable[complement]]
        else:
            hashtable[num] = i

    return [-1,-1]
'''
正确性：8/10 (使用 nums_list.index(num) 可能会导致在数组中有重复元素时返回错误的索引。分数：)
可读性：7/10 (代码结构清晰，变量命名合理，但缺少注释。)
效率：
时间复杂度：O(n)。分数：10/10
空间复杂度：O(n)。分数：8/10
->使用 enumerate 函数来同时获取数组元素和其索引
'''

#4_1 优化
def def4_1(nums,target):
    target_int = int(target)
    nums_str = nums.split(",")
    nums_list = list(map(int,nums_str))
    hashtable = {}

    for index,num in enumerate(nums_list):
        #print(f"index:{index} || num:{num}")       #checkpoint
        complement = target_int - num
        if complement in hashtable:
            return [hashtable[complement],index]
        else:
            hashtable[num] = index

    return [-1,-1]
'''
总评分：9.3/10
'''

#main()
nums = input("数组")
target = input("目标数值")
print(def4_1(nums,target))