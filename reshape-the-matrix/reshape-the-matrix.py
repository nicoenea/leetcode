import numpy
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c == len(mat) * len(mat[0]):
            return numpy.reshape(mat,(r,c))
        else:
            return mat
        
        
        