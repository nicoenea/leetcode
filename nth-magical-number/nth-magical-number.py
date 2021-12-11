class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lo=2
        hi=10**100
        while(lo<=hi):
            mid=(lo+hi)//2
            if mid//a + mid//b - mid//((a*b)//math.gcd(a,b))>=n:
                res=mid
                hi=mid-1
            else:
                lo=mid+1
        return res%(10**9+7)