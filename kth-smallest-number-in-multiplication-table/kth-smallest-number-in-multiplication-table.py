class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n: # swapping the value of m and n has no influence on the results, since the table is symmetric
            m, n = n, m

        # count the number elements that are lower than number 
        def search(number):
            ans = 0
            for i in range(1,min(m, number) + 1):
                ans += min(n, number // i)
            return ans
        # binary search    
        left = 1
        right = m * n
        while left < right:
            mid = (left + right) // 2
            if search(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
        