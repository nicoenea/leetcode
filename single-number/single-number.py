class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Beeg Brain Approach
        """
        return 2 * sum(set(nums)) - sum(nums)
        """
        First Approach:
        
        very ineffective, not linear time
        """
        for num in nums:
            if nums.count(num) == 1:
                return num
