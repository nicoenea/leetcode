class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr: return None
        if len(arr) == 1: return [-1]
        
        n = len(arr)
        res = [None] * n
        
		# we start at the end of the array and end at index 0
		# i = n - 1 to i = 0, decrementing by 1 each iteration
        for i in range(n - 1, -1, -1):
            # at the last index, the value remains the same
            # until the end
            if i == n - 1:
                res[n - 1] = arr[n - 1]
            # otherwise, the results array for index i
            # is precisely the greater of the next index's result value
            # and the next index's value itself
            else:
                res[i] = max(arr[i + 1], res[i + 1])
        
        # set the last index to -1 and return
        res[-1] = -1
        
        return res
                
                