class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0 
        
        for index, val in enumerate(flowerbed):
            
            if (flowerbed[index] == 0 and (index == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] ==0)):
                flowerbed[i] = 1
                count += 1
            
            i += 1 
        
        return count >= n