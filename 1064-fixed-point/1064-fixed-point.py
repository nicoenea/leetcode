class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        # Iterate through array. If index == val, return val
        for index, val in enumerate(arr):
            if index == val:
                return val
        # Return -1 after done iterating, meaning that there is no value == index number
        return -1
        