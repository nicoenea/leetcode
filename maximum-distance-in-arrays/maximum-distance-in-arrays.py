class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Brute Force
        ans = 0
        maxNum = float("-inf")
        minNum = float("inf")
        
        for array in arrays:
            ans = max(ans, array[-1]- minNum, maxNum - array[0])
            minNum, maxNum = min(minNum, array[0]), max(maxNum, array[-1])
            
        return ans