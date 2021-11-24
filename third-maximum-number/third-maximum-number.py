class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sSet = sorted(set(nums)) 
        if len(sSet) < 3:  # If the length of the list is less than 3, there is no third maximum
            return sSet[-1] # so we return the max 
        else:    
            return sSet[-3]
        