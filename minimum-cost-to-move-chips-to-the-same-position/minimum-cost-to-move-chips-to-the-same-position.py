class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        
        dictionary = defaultdict(int)
        for i in position:
            dictionary[i % 2] += 1
            
        return min(dictionary[1], dictionary[0])