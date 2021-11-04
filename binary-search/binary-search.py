class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Approach #1:
        1. define 'matchCount' as a flag to tell if there was a match to 'target' in our list.
        2. Iterate through list index by using enumerate() to get index
        3. if nums[i] is equal to target, we increase matchCount to indicate that we have found a match
        4. Once for loop is finished, check if there was a match, or else return -1
        """
        matchCount = 0 # 1
        for i, _ in enumerate(nums): # 2
            if nums[i] == target: # 3
                matchCount += 1
                return i
        if matchCount == 0: #4
            return -1
