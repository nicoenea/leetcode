class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        
        c = Counter(s)
        pos = 0
        
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            c[s[i]] -= 1
            if c[s[i]] == 0:
                break
        
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''