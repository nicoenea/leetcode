class Solution:
    def firstUniqChar(self, s: str) -> int:
        for charIndex in range(0, len(s)):
            if s.count(s[charIndex]) == 1:
                return charIndex
        return -1