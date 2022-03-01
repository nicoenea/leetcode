class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1)
        count=0
        count2 = 0
        while count < m+n:
            if count >= m:
                nums1[count] = nums2[count2]
                count2+=1
            count+=1
        nums1.sort()