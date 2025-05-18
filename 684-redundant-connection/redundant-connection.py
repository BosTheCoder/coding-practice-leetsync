class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]

        def union(node1, node2):
            # print(f"before union {parent} {rank}")
            if rank[node1] > rank[node2]:
                parent[node2] = node1
                rank[node1] += rank[node2]
            else:
                parent[node1] = node2
                rank[node2] += rank[node1]
            # print(f"after union {parent} {rank}")

        def find(node):
            while parent[node] !=node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return parent[node]
        
        for node1, node2 in edges:
            parent1, parent2 = find(node1), find(node2)
            # print(parent1, parent2)
            if parent1 == parent2:
                return [node1,node2]
            
            union(parent1,parent2)
        return [-1,-1]
        