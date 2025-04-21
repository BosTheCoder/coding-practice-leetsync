class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # check horizontal
        for j in range(len(board)):
            hash = set()
            for i in range(len(board[0])):
                val = board[j][i]
                if val == ".":
                    continue
                if val in hash:
                    return False
                hash.add(val)

        # check vertical
        for i in range(len(board[0])):
            hash = set()
            for j in range(len(board)):
                val = board[j][i]
                if val == ".":
                    continue
                if val in hash:
                    return False
                hash.add(val) 
        
        def get_block(i,j):
            return (i//3,j//3)
        
        block_sets = defaultdict(set)

        # check squares
        for j in range(len(board)):
            for i in range(len(board[0])):
                val = board[j][i]
                if val == ".":
                    continue
                block = get_block(i,j)
                if val in block_sets[block]:
                    return False
                block_sets[block].add(val)
        return True