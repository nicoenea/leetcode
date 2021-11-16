class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ## 2 Pointer Approach
        """
        Time Complexity:  O(NlogN)
	    Space Complexity: O(1) 
        """
		
        indx1 = 0
        indx2 = 0
        intersections = []
        # Sort lists before putting through while loop to do 2 pointer approach
        nums1.sort() # sort() uses Timsort Algorithm 
        nums2.sort()
        
        while indx1 < len(nums1) and indx2 < len(nums2):
            
                
            if nums1[indx1] < nums2[indx2]:
                indx1 += 1
                continue # add continue to make it check again after index+=1
            if nums2[indx2] < nums1[indx1]:
                indx2 += 1
                continue
            intersections.append(nums1[indx1])
            indx1 += 1
            indx2 += 1
        return intersections