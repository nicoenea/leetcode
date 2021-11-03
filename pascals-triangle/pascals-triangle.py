class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # initialize Triangle with the number of rows
        pTriangle = [0] * numRows
        
        for i in range(numRows):
            pTriangle[i] = [0] * (i + 1) # fill each row with its respective amonut of columns
            pTriangle[i][0] = 1 # set leftmost row index to 1
            pTriangle[i][i] = 1 # set rightmost row index to 1
            
            # Add numbers to fill in inside of trangle
            for j in range(1 , i):
                pTriangle[i][j] = pTriangle[i-1][j-1] + pTriangle[i-1][j]
        return pTriangle
