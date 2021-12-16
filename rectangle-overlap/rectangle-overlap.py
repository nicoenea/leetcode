class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        o_x1 = max(rec1[0], rec2[0]) 
        o_x2 = min(rec1[2], rec2[2])  
        o_y1 = max(rec1[1], rec2[1])
        o_y2 = min(rec1[3], rec2[3]) 

        if o_x1 < o_x2 and o_y1 < o_y2:
            if (o_x2 - o_x1) * (o_y2 - o_y1) > 0:
                return True
        return False
