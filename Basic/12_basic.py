<<<<<<< HEAD
def quickSort(self, arr, left, right):
    if left >= right:
        return

    pivot = partition(arr,left,right)
    quickSort(arr,left,pivot-1)
    quickSort(arr,pivot,right)

def partition(self, arr, left, right) -> int:
    pivot = arr[right]

    index = left
    for i in range(left,right):
        if arr[i] <= pivot:
            

    i = left -1
    for (int j = start )
    return i
=======
'''
标准的基本方法
'''
def quickSort (arr,left,right):
    if left < right:
        pivot = partition(arr,left,right)

        quickSort(arr,left,pivot - 1)
        quickSort(arr,pivot + 1 ,right)

def partition(arr,left,right):
    pivot = arr[right]
    j = right
    i = left - 1

    for j in range(left,right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        
    arr[i + 1], arr[right]  = arr[right], arr[i + 1]
    return i + 1

arr=[10,7,8,9,1,5]
quickSort(arr,0,len(arr)-1)
print(arr)

'''
不稳定排序
时间复杂度: O(nlogn)，  最坏O(n^2)
空间复杂度:  O(logn)
'''
>>>>>>> 611ed2ce1f9686e6f20ea6bd5ecca3a3cd0f315b
