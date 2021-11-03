class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
               
        return sum([[k] * min(n, cnt2[k]) for k, n in cnt1.items() if k in cnt2], [])