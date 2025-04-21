class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node:int) -> int:
            """find the root of a node"""

            while par[node] != node:
                par[node] = par[par[node]]
                node = par[node]
            
            return node
    

        def union(n1:int, n2:int) -> int:
            """Return 0 if unsuccesfull & 1 if succesfuull"""
            r1,r2 = find(n1), find(n2)

            if r1 == r2:
                return 0
            
            if r1>r2:
                par[r2] = r1
                rank[r1] += rank[r2]
            else:
                par[r1] = r2
                rank[r2] += rank[r1]
            
            return 1
        
        total_components = n
        for n1, n2 in edges:
            total_components -= union(n1,n2)
        
        return total_components