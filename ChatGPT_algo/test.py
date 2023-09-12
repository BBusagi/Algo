# 原始列表
nums = [4, 2, 1, 9, 5]

# 配对元素与其原始索引
indexed_nums = [(num, index) for index, num in enumerate(nums)]
print(indexed_nums)
# 根据元素值进行排序
indexed_nums.sort()
print(indexed_nums)
# 提取排序后的原始索引
sorted_indices = [index for num, index in indexed_nums]

print("排序后的原始索引:", sorted_indices)
