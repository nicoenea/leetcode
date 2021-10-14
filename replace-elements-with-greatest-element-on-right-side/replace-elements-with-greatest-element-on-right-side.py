class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr=arr[::-1]
        maxNum=-1
        for i in range(len(arr)):
            print(arr[i])
            tmp=arr[i]
            arr[i] = maxNum
            if tmp > maxNum:
                maxNum=tmp
        return arr[::-1]
                
        