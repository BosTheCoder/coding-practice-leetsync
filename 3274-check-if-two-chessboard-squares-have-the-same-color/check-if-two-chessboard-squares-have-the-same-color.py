class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def color(c1: str) -> str:
            oddcols = {"a","c","e","g"}
            col, row = c1[0], int(c1[1])
            if (col in oddcols and row%2 == 1) or (col not in oddcols and row%2 == 0):
                color = "black"
            else:
                color = "white"
            print(c1, color)
            return color
        
        return color(coordinate1) == color(coordinate2)
