class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
            1. Put all possible integers in a dictionary.
            2. init integer variables to store our converted strings
            3. iterate through the strings, and put all the digits back together as int 
                3a. Multiply previous iteration by 10 to make space for the next digit
            4. Return product of both ints, converted back to string
        """
        
        intDict = { # 1
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8, 
            '9' : 9,
        }
        int1 = 0 #2
        int2 = 0
        
        for char in num1: #3
            print("before: ", int1)
            int1 = intDict[char] + (10 * int1)
            print("after: ", int1)
        for char in num2:
            int2 = 10 * int2 + intDict[char]
        print(int1, int2)
        return str(int1 * int2) #4
        
        
        """
        Easy one-line Solution: 
        (goes against the problem description but still accepted by judge)
        """
        #return str(int(num1) * int(num2))
        
