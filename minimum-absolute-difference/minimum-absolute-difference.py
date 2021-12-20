class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        minDiff = 10000000000000000
        for i in range(len(arr)-1):
            minDiff = min(minDiff, arr[i+1] - arr[i])
        
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == minDiff:
                ans.append([arr[i], arr[i+1]])
        return ans