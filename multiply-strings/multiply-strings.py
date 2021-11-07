class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Put all possible integers in a dictionary
        intDict = {
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
        #init integer variables to store our converted strings
        int1 = 0
        int2 = 0
        
        # iterate through string, and put all digits back together as int 
        for char in num1:
            int1 = 10 * int1 + intDict[char]
        for char in num2:
            int2 = 10 * int2 + intDict[char]
        
        # return product of both ints, converted to string
        return str(int1 * int2)