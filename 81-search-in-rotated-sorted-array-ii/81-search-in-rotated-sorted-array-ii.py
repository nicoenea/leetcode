class Solution:
    def search(self, L: List[int], target: int) -> int:
        """
        Search in Rotated Sorted Array II

        time: O(logn)
        space: O(1)

        :param List[int] L:
        :param int target:
        :return int:
        """
        N = len(L)

        lo = 0
        hi = N - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target == L[mid]:
                return True

            elif L[lo] == L[mid] == L[hi]:
                lo += 1
                hi -= 1

            elif L[lo] <= L[mid]:
                if L[lo] <= target < L[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # elif L[mid] <= L[hi]:
            else:
                if L[mid] < target <= L[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
        