class Solution:
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        ptr1, ptr2 = 0, 0
        
        while ptr1 < len(firstList) and ptr2 < len(secondList): # iterate through both lists
            
            start = max(firstList[ptr1][0], secondList[ptr2][0])
            end = min(firstList[ptr1][1], secondList[ptr2][1])
            
            if start <= end: # if there is an interval, append it to list
                ans.append([start,end])
            if firstList[ptr1][1] < secondList[ptr2][1]: # move pointers accordingly
                ptr1 += 1
            else: 
                ptr2 += 1
            
        return ans 
    
    
    # O(N+M) Time 
    # O(1) Space
