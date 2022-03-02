class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index, val in enumerate(nums):
            nums[index] *= val
            
        nums.sort()   
        
        return nums