class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        for index, val in enumerate(s): #iterate through string
            if s.count(val) == 1: # this will find the first char that is unique
                return index # return index of char
            
        return -1 # if we finished the iteration and didn't find anything, return -1