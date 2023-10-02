'''
py 简化算法
利用了列表推导式
'''
def quickSort (arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot ]
    right = [x for x in arr[1:] if x > pivot]

    return quickSort(left) + [pivot] + quickSort(right)

arr=[10,7,8,9,1,5]
arr2 = quickSort(arr)
print(arr2)

'''
不稳定排序
时间复杂度: O(nlogn)，  最坏O(n^2)
空间复杂度:  O(n)
'''
