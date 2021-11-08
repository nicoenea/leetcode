class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach 2:
        
        Sliding window: Use a dictionary to store chars, move pointer when a repeated               
            character is in your window
        
            1. Iterate through string (right pointer)
            2. if s[RightPointer] is not in seen, increase window size by moving pointer
            3a. s[rightPointer] is in our current window, so we move our leftPointer forward
            3b. s[RightPointer] is not in current window, so we move RightPointer
                    forward to increase the window
                    
           Time Complexity: O(N)
           Space Complexity: O(N)
            
        """
        seen = {}
        leftP = 0
        output = 0
        
        for rightP in range(len(s)): # 1
            if s[rightP] not in seen: # 2 
                output = max(output, rightP - leftP + 1)
            else:
                if seen[s[rightP]] < leftP: # 3a
                    output = max(output, rightP - leftP + 1)
                else: # 3b
                    leftP = seen[s[rightP]] + 1
            seen[s[rightP]] = rightP
        
        return output
    
    
            
#         maxLen = 0      # we set maxLen to 0 because string may be empty.
#         seenChar = '' # a empty string to store the character that we have already seen.
        
#         for char in s:   # we are checking every char/character in string...
#             if char not in seenChar:
#                 seenChar += char      # if char not in there then we add to it.
                
#             else:
#                 ## now if the char is already in seenChar then we get the index of that char by using seenChar.index() and then we slice the string from that index+1 to last, so that the the first seen char will be removed.
#                 # for example - 'abcabbd'     # here after 'abc' , again "a" was there so we get the index of first "a" and slice the string then be get string = "bc" .
#                 seenChar = seenChar[seenChar.index(char) + 1:] + char
#                 # and then we add the char "a" to the last. so the string will become "bca"
                
#             maxLen = max(maxLen, len(seenChar))   # here we use a function max() that everytime return the maximum value between two number. it sets maxLen each time the loop runs.
#         return maxLen     # finally return the maximum length.