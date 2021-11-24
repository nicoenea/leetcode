class Solution:
    
    def findInterval(val1, val2):
        pointer = 0
        if val1[1] > val2[1]: 
            pointer = 2
        else: pointer = 1
            
        if val1[0] > val2[1] or val2[0] > val1[1]: # if the given closed intervals don't match, there is no interval
            return [], pointer # returning empty 
        
        start = max(val1[0], val2[0]) #find start and end of interval
        end  = min(val1[1], val2[1])
        return [start, end], pointer
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        pt1 = pt2 = 0
        
        while pt1 < len(firstList) and pt2 < len(secondList): # iterate through both lists
            
            interval, pointer = Solution.findInterval(firstList[pt1], secondList[pt2]) # use function to find interval
            
            if interval:  # append intervals to ans
                ans.append(interval)
            if pointer == 1: # increase pointer
                pt1 += 1
            else:
                pt2 += 1
            
        return ans