class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for num in nums:
            if num == 1:
                count +=1
                if maxCount <= count:
                    maxCount = count

            else:
                count = 0
                
        return maxCount