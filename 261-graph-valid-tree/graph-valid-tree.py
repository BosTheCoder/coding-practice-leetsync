class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        
        # create adj list
        adj_list = {}
        for src, dest in edges:
            adj_list.setdefault(src, []).append(dest)
            adj_list.setdefault(dest,[]).append(src)
        
        seen = set()
        q = Deque([0])
        while q:
            node = q.popleft()
            if node in seen:
                continue

            seen.add(node)
            for neighbour in adj_list.get(node,[]):
                q.append(neighbour)
            
        return len(seen) == n
