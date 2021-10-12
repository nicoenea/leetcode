class Solution:
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        
        for start in range(len(arr)-1):
            if arr[start+1] <= arr[start]:
                break
                
        for end in range(len(arr)-1, 0, -1):
            if arr[end-1] <= arr[end]:
                break
                
        return start == end
    
    
    # O(n) time complexity
