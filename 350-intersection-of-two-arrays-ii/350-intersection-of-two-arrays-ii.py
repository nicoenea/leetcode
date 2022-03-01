class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pt1 = 0
        pt2 = 0
        intersection = []
        
        nums1.sort()
        nums2.sort()
        
        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] < nums2[pt2]:
                pt1 += 1
                continue
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
                continue
                
            intersection.append(nums1[pt1])
            pt1+=1
            pt2+=1
            
        return intersection