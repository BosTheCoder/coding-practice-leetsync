class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        while l <= r:
            mid = (l+r) //2
            if target == matrix[mid][0]:
                return True
            if target > matrix[mid][0]:
                l = mid + 1
            else:
                r = mid -1
        
        row = r

        # searching row
        l,r = 0, len(matrix[row])-1
        while l <= r:
            mid = (l+r) //2
            if target == matrix[row][mid]:
                return True
            if target > matrix[row][mid]:
                l = mid + 1
            else:
                r = mid -1
        return False

"""
        
r   l     
1 , 10,  23
m
"""