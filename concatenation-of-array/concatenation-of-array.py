class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concatenated = [None] * (2 * len(nums))
        for i in range(0, len(nums)):
            concatenated[i] = nums[i]
            concatenated[i + len(nums)] = nums[i]
            
        return concatenated