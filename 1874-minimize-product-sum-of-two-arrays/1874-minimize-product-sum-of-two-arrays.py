class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        productSum = 0
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2, reverse=True)
        
        for num in range(0, len(nums1)):
            productSum += nums1[num] * nums2[num]
            
        return productSum
            
            