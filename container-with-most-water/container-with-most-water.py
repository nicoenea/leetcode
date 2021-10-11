class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftP = 0
        rightP = len(height)-1
        res = 0
        while leftP < rightP:
            area = (rightP - leftP) * min(height[leftP], height[rightP])
            res = max(area,res)
            if height[leftP]<height[rightP]:
                leftP = leftP+1
            else:
                rightP = rightP-1
        return res
            