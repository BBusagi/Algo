import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            minHeap.append([x**2 + y**2, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            # .heappop 保证了每次取出的都是当前堆中的最小元素
            dist,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            
            # 从 minHeap 的尾部取出，不考虑它是否是最小的。这样做不保证取出的元素是当前列表中的最小值，并且
            # 这样操作后，minHeap 不再具有堆的性质。
            # temp = minHeap.pop()
            # res.append([temp[1],temp[2]])

            k -= 1
        
        return res
