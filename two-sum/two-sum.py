class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i
                
"""
 range(len(list)) can be replaced by using "enumerate()" as seen below 
"""               
                
                
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
        
#         for i in range(len(nums)):
#             print(i, nums[i])
#             remaining = target - nums[i]
            
#             if remaining in seen:
#                 return [i, seen[remaining]]
#             else:
#                 seen[nums[i]] = i