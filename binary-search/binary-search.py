from bisect import bisect_left ,bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Approach #5: (Thanks to geeksforgeeks)
        
        use bisect_left()
                requires import statement: from bisect import bisect_left, bisect
                
        This one has achieved the highest time complexity efficiency so far (faster than 99.42%)
        """
        if bisect_left(nums, target)!=bisect(nums, target):
            return nums.index(target)
        else:
            return -1
        
        """
        Approach #4:
        
        use count() to check if the target exists in our list
        
        Same time complexity as Approach #3
        """
#         count_target = nums.count(target)
        
#         if count_target == 0:
#             return -1
#         else:
#             return nums.index(target)
       
        
        """
        Approach #3:
        
        Python can check for 'x' value in a list.
        
        Time complexity was greatly improved
        """
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        
        """
        Approach #2:
        
        There is no need to init a variable to keep track of whether there was a target on our list.
            If there is a target, our for loop will automatically end by returning the index of our target match
            Else, the for loop will keep going, until it reaches the end and returns -1 anyway
            
        In the end we just need to:
            1. Iterate through list index (by using enumerate()) 
            2. If nums[i] is equal to target, return index value
            3. Else for loop will continue running and return -1 at end
        
        THIS DID NOT MAKE ANY DIFFERENCE TO TIME/SPACE complexity, but it beautified the code slightly
        
        #TODO: there might be a better way of iterating through the list instead of using enumerate()
        """
        # for i, _ in enumerate(nums): # 2
        #     if nums[i] == target: # 3
        #         return i
        # return -1
        
        """
        Approach #1:
        1. define 'matchCount' as a flag to tell if there was a match to 'target' in our list.
        2. Iterate through list index by using enumerate() to get index
        3. if nums[i] is equal to target, we increase matchCount to indicate that we have found a match
        4. Once for loop is finished, check if there was a match, or else return -1
        """
        # matchCount = 0 # 1
        # for i, _ in enumerate(nums): # 2
        #     if nums[i] == target: # 3
        #         matchCount += 1
        #         return i
        # if matchCount == 0: #4
        #     return -1
