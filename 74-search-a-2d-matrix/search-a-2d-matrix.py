class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_cols = [row[0] for row in matrix]
        ix = bisect.bisect_left(first_cols, target)

        # Check if we've found value
        if ix <len(first_cols) and first_cols[ix] == target:
                return True
        
        # If less than first value than it's not in matrix
        if ix == 0:
            return False
        
        row = matrix[ix-1]

        new_ix = bisect.bisect_left(row,target)

        # Check if we've found value in row
        if new_ix<len(row) and row[new_ix] == target:
            return True
        else:
            return False
