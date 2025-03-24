class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        seen = set()

        def dfs(r, c, i):

            if board[r][c] != word[i] or (r,c) in seen:
                return False
            
            if i == len(word) -1:
                # print("Found you", r, c)
                return True
            
            seen.add((r,c))
            i+=1
            for d in directions:
                row,col = r+d[0], c+d[1]
                if 0<=row<len(board) and 0<=col<len(board[0]):
                    if dfs(row, col, i):
                        return True
            
            seen.remove((r,c))
            return False
            
                
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and dfs(r, c, 0):
                        return True
        return False