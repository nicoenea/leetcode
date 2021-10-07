class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evenCount = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                evenCount+= 1
        return evenCount
                
            