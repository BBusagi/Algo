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