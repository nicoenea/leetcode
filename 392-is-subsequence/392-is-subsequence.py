class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer solution
        
        left_end, right_end = len(s), len(t)
        left_p = right_p = 0
        
        while left_p < left_end and right_p < right_end:
            # move both or just one pointer
            if s[left_p] == t[right_p]:
                left_p+=1
            right_p+=1
            
        return left_p == left_end
        