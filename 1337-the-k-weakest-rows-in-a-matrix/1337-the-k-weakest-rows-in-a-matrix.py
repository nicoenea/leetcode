class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        # Build a list of (strength, index) pairs.
        strengths = [(sum(row), i) for i, row in enumerate(mat)]


        # Sort.
        strengths.sort()

        # Pull out and return the indexes of the first k entries.
        return [i for strength, i in strengths[:k]]