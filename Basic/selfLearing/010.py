'''
在 Python 中，heapq 模块提供了一个 heapify 函数，
该函数用于将列表转换为一个有效的堆数据结构（默认为最小堆）。
'''

import heapq

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(data)
print(data)
