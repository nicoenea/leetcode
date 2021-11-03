import numpy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
            Check if the size of the matrix  == size of the matrix to be returned
            
            len(mat) == number of rows (r)
            len(mat[0]) == number of columns (c)
        """
        if r*c == len(mat) * len(mat[0]):
            print(r*c, len(mat)*len(mat[0]))
            return numpy.reshape(mat,(r,c))
        else:
            return mat
        
        
        
