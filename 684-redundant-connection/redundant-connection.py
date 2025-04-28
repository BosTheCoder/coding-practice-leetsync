class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        num_nodes = len(edges)
        parent = [i for i in range(num_nodes)]
        rank = [1] * num_nodes
        
        def find(n):
            node = n-1
            while parent[node] != parent[parent[node]]:
                parent[node] = parent[parent[node]]
            return parent[node] + 1

        def union(n1, n2):
            node1, node2 = n1-1, n2-1

            if rank[node1] > rank[node2]:
                rank[node1] += rank[node2]
                parent[node2] = node1
            else:
                rank[node2] += rank[node2]
                parent[node1] = node2

        
        for n1,n2 in edges:
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return [n1, n2]
            
            union(p1, p2)
        
        return []



