class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        tempList = [0] * len(nums)
        for num in range(len(nums)):
            tempList[num] = nums[num] * nums[num]
        nums = sorted(tempList, key=int)        
        return nums