class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            if any(x.isalpha() for x in s):
                res = max(res, len(s))
            else:
                res = max(res, int(s))
        return res
