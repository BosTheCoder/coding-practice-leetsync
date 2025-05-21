class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height, width = len(matrix), len(matrix[0])
        def setflag(j,i,flag):
            # print(f"setting flag for item {j},{i}")
            for col in range(width):
                if matrix[j][col] == 0 and col != i:
                    continue
                matrix[j][col] = flag
                
            for row in range(height):
                if matrix[row][i] == 0 and row != j:
                    continue
                matrix[row][i] = flag
            # print(matrix)
        
        # print(matrix)
        flag = "c"
        for j in range(height):
            for i in range(width):
                if matrix[j][i] == 0:
                    # print(f"found {matrix[j][i]}")
                    setflag(j,i,flag)
        
        for j in range(height):
            for i in range(width):
                if matrix[j][i] == flag:
                    matrix[j][i] = 0