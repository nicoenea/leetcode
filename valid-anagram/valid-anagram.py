class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = False
        falseCount = 0
        longest = None
        smallest = None
        if len(t) > len(s):
            longest = t
            smallest = s
        else:
            longest = s
            smallest = t
        for char in longest:
            if char not in smallest or longest.count(char) != smallest.count(char):
                falseCount += 1
                
        if falseCount == 0:
            return True
        else: return False
        
            