# Definition for a pair.
from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        for i in range(n):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key :
                pairs[j] , pairs[j + 1] = pairs[j + 1] , pairs[j]
                j -= 1
            
            #show output
            res.append(pairs[:]) #添加副本
            #res.append(pairs) #添加本体，相同引用地址

        return res