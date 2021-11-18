class Solution:
    def findDisappearedNumbers(self, n: List[int]) -> List[int]:
    	N = set(n)
    	return [i for i in range(1, len(n) + 1) if i not in N]