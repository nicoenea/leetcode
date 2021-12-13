class Solution:
    def maxPower(self, s: str) -> int:
        count = maxCount = 0
        previous = ""
        
        for char in s:
            
            if char == previous:
                count += 1
            else:
                count = 1
                previous = char
            maxCount = max(maxCount, count)
        
        return maxCount