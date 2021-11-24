class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sHeights = sorted(heights)
        ans = 0
        for index, val in enumerate(heights):
            if heights[index] != sHeights[index]: # if original list order doesn't match the sorted list order
                ans += 1  # adds to count of mismatched indices
                
        return ans