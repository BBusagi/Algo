'''
归并排序(arr):
1. 如果 arr 的长度小于等于 1，则直接返回 arr，因为长度为 1 或 0 的数组已经是排序好的。
2. 计算数组的中点。
3. 把数组分为两个部分：left 从开始到中点，right 从中点到结束。
4. 对 left 部分进行归并排序。
5. 对 right 部分进行归并排序。
6. 合并排序好的 left 和 right，得到排序好的数组。
7. 将原本的数组的无序数组更换为排序后的数组。       #重点 不是改变引用 而是对象本身 -> 11_tip.md
8. 返回排序好的数组。

合并(left, right):
1. 创建一个空数组 result。
2. 当 left 和 right 都有元素时：
    1. 如果 left 的第一个元素小于 right 的第一个元素，把 left 的第一个元素加到 result 里，并移除 left 的第一个元素。
    2. 否则，把 right 的第一个元素加到 result 里，并移除 right 的第一个元素。
3. 当 left 还有元素时，把 left 的元素加到 result 里。
4. 当 right 还有元素时，把 right 的元素加到 result 里。
5. 返回 result。
'''

def mergeSort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]
    
    mergeSort(left)
    mergeSort(right)
    merged = merge(left, right)
    for i in range(len(merged)):
        arr[i] = merged[i]

    return arr


def merge(left,right):
    res = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1

    while j < len(right):
        res.append(right[j])
        j += 1
    
    return res

#arr = [38, 27, 43, 3, 9, 82, 10]
arr = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_arr = mergeSort(arr)
print(sorted_arr)\

'''
时间复杂度: O(nlogn)
空间复杂度: O(n)
'''