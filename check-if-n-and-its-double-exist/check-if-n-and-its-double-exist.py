class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1: return True #
        setArr = set(arr) - {0} #turn list into set to remove zeros
        for num in arr:
            if 2*num in setArr: return True
        return False