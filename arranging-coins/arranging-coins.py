class Solution:
    def arrangeCoins(self, n: int) -> int:
        rowLen = 1
        rowCount = 0
        while n >= 0:
            n = n - rowLen
            rowCount += 1
            rowLen += 1
        return rowCount -1