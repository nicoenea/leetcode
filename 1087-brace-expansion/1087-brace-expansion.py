class Solution:
    def expand(self, s: str) -> List[str]:
        A = s.replace('{', ' ').replace('}', ' ').strip().split(' ')
        B = [sorted(a.split(',')) for a in A]
        return [''.join(c) for c in itertools.product(*B)]
            