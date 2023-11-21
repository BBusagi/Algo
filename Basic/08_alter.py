class Solution:
    def countComponents(self, n, edges) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            #查询是否为自身，如果不是则追溯根结点
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            #确认是否为根结点
            p1, p2 = find(n1), find(n2)

            #如果根结点相同，即已经相连
            if p1 == p2:
                return 0
            
            #合并 小的并到大的
            # case1 p2较大 p1的根应该为p2
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            # case2 p1较大 p2的根应该为p1
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        res = n
        for n1,n2 in edges:
            res -= union(n1,n2)
        return res
    

# Test Case:
sol = Solution()
edges = [[0, 1], [1, 2], [3, 4]]
#edges = [[0, 1], [1, 2], [2, 3], [3, 0]]
n = 5
print(sol.countComponents(n, edges))  
# Expected output: 2 (一个连通组件是0-1-2-3, 另一个是孤立的节点4)
