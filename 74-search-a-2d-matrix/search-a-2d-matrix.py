class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)

        while l<r:
            mid = l+(r-l)//2

            if matrix[mid][0]>target:
                r=mid
            else:
                l = mid + 1

        if l==0:
            return False
        
        row = matrix[l-1]

        i = bisect_left(row,target)

        return i<len(row) and row[i] == target

