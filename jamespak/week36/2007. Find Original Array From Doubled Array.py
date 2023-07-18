class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        d = defaultdict(int)
        res = []
        for n in sorted(changed, reverse=True):
            if n*2 in d:
                d[n*2] -= 1
                if d[n*2] == 0:
                    del d[n*2]
                res.append(n)
            else:
                d[n] += 1
        return res if len(d) == 0 else []
