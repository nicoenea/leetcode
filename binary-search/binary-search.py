class Solution:
    def search(self, nums: List[int], target: int) -> int:
        matchCount = 0
        for i, _ in enumerate(nums):
            if nums[i] == target:
                matchCount += 1
                return i
        if matchCount == 0:
            return -1