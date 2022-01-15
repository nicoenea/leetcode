class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
       
        rows = len(matrix)
        columns = len(matrix[0])
        answer = 0

        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 1: # for 1x1 squares
                    if row == 0 or col == 0:
                        answer += 1

                    else:  # rest of the square types
                        val = min(matrix[row-1][col-1], matrix[row][col-1], matrix[row-1][col]) + matrix[row][col]
                        answer += val
                        matrix[row][col]  = val

        return answer