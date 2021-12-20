class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        setList = set(nums)
        for num in setList:
            if nums.count(num) > len(nums)/2:
                return num