class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for index in range(len(nums)): # iterate through list index
            if index != 0: # omit 0 index
                nums[index] += nums[index-1] # add previous value to current value
        return nums