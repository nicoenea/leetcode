class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        l = len(arr)
        zeroes = 0
        for item in arr:
            if(item==0):
                zeroes += 1
        i = l-1
        j = l-1+zeroes
        while(j>0):
            if(arr[i]==0):
                if(j<l):
                    arr[j] = 0
                j -= 1
            if(j<l):
                arr[j] = arr[i]
            i -= 1
            j -= 1
    
                
      
        """
        Do not return anything, modify arr in-place instead.
        """
        