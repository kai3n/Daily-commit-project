class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = set()
        def helper(s, d, cur, res):
            if not s:
                return
            if d == 0:
                if len(s) > 1 and s[0] == '0':
                    return
                if 0 <= int(s) <= 255:
                    res.add(".".join(cur + [s]))
                return
            for i in range(1, 4):
                if 0 <= int(s[:i]) <= 255:
                    if i > 1 and s[0] == '0':
                        return
                    helper(s[i:], d - 1, cur + [s[:i]], res)
        helper(s, 3, [], res)
        return res
