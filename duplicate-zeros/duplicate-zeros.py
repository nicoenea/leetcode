class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n= len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr[i+1:n] = arr[i:n-1]
                i +=2
            else: i+=1
                
      
        """
        Do not return anything, modify arr in-place instead.
        """
        