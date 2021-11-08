class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Current Approach:
        
        Python Knowledge
        """
        # Even though s = s[::-1] will print out the correct answer, 
        #   using s[:] = s[::-1] will actually modify the bytes in place
        s[:] = s[::-1] 
        
        """
        Previous approach: cheating
        """
        # s.reverse()
        
        
        """
        First Try:
        """
        # i = 0 #// from left to right
        # j = len(s) - 1 #//from right to left
        # while(i < j): # // stop until meet
        #     tmp = s[i];
        #     s[i] = s[j];
        #     s[j] = tmp;
        #     i+=1;
        #     j-=1;
