class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tempList = [0] * len(nums) #Give tempList the same length as original nums List
        
        for i in range(len(nums)):
            tempList[(i + k) % len(nums)] = nums[i]
            # use (i + k) % len(nums) to determine the position the number should be in 
            #   after moving k steps to the right
            # = nums[i] to copy the original value to its new designated k-steps to the right position
            
            
        nums[:] = tempList # copy tempList to nums
        #use [:] to delete items in original list, and then replace with items in tempList
                
                
        """
        Do not return anything, modify nums in-place instead.
        """
        