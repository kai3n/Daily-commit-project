class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        def dfs(s, cur):
            if not s:
                if eval(cur) == target:
                    res.append(cur)
                    return
            
            for i in range(len(s)):
                w = s[:i + 1]
                if w and len(w) > 1 and w[0] == '0':
                    continue
                if cur:
                    for op in "+-*":
                        dfs(s[i + 1:], cur + op + w)
                else:
                    dfs(s[i + 1:], w)
        dfs(num, '')
        return res
