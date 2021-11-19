class Solution:
    def romanToInt(self, s: str) -> int:
        # Use dictionary to translate  string into int values
        dicts = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        result = 0
        prev_val = 0 # keep track of previous value to adjust for roman numeral position
        for char in s:
            value = dicts[char]
            result += value
            if value > prev_val: # subtract the prev value multiplied by 2 to undo the previous operation and get the value correctly
                result -= 2 * prev_val
            prev_val = value
        return result