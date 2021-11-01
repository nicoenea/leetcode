class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0, n): # Iterate through second array length: 0 -> n
            nums1[i + m] = nums2[i] # add m to current index to get nums2 value into nums1 respective index location
        nums1.sort() #sort nums1 to get final answer
        """
        Do not return anything, modify nums1 in-place instead.
        """
        