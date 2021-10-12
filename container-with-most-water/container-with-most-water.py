class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        left, right = 0, len(height)-1
        area_max = 0
        
        while left < right:   
            
            if height[right] >= height[left]:
                area = (right-left) * height[left]
                left = left+1 
                
                if area > area_max:
                    area_max = area     
                
            else: 
                area = (right-left) * height[right]
                right = right -1
                
                if area > area_max:
                    area_max = area
                    
        return area_max
        