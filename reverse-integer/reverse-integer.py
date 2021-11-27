class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0:
            numList = [str(char) for char in str(x)]
            ans = int(''.join(reversed(numList)))
        else:
            conv = str(x)
            conv = split('-', conv)[1]
            numList = [str(char) for char in str(conv)]
            ans = - int(''.join(reversed(numList)))
        if ans.bit_length() > 31:
            return 0
        return ans