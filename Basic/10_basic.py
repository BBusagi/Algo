'''
插入排序
将未排序的元素逐个插入到已排序的部分，
每次插入都会将元素移动到其正确的位置，直到整个数组都排好序为止。

稳定的排序算法
适用于小型数据集或已接近排序状态的数据集
'''

'''
插入排序(arr):
1. 遍历数组，从第二个元素开始，记为 curr。
2. 把 curr 处的元素记为 key
3. 比较 key 与前一个元素：
    1. 如果 key 小于前一个元素，则交换它们。
    2. 继续与前一个元素比较，直到 key 大于前一个元素或已经没有前一个元素。
4. 继续下一个 curr 直到数组结束。
5. 返回已排序的 arr。

'''
def insertionSort(arr):
	for curr in range(1, len(arr)):	#curr
		key = arr[curr]
		j = curr-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

my_list = [12, 11, 13, 5, 6]
insertionSort(my_list)
print("Sorted array:", my_list)

'''
算法复杂度
时间复杂度：O(n) ~ O(n^2), avg: O(n^2)
空间复杂度：O(1)
'''