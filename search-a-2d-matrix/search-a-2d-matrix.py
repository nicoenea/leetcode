class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix: # iterate through rows of matrix
            if target in row: # if target in row, return true
                return True
        return False # if finished iterating, it means we don't have target in matrix, so return False