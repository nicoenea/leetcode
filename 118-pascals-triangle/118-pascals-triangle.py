class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pTriangle = [0] * numRows
        
        for row in range(numRows):
            pTriangle[row] = [0] * (row + 1) # fill rows with num of columns
            pTriangle[row][0] = 1 # fill left side with 1
            pTriangle[row][row] = 1 # fill right side with 1
            
            for inside in range(1, row):
                pTriangle[row][inside] = pTriangle[row - 1][inside - 1] + pTriangle[row - 1][inside]
            
        return pTriangle