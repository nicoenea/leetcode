class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index, val in enumerate(nums):
            hashmap[nums[index]] = index
        for index, val in enumerate(nums):
            complement = target - nums[index]
            if complement in hashmap and hashmap[complement] != index:
                return [index, hashmap[complement]]