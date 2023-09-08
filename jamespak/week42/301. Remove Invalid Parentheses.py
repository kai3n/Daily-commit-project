class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        
        queue = {s}
        while queue:
            res = []
            for node in queue:
                if is_valid(node):
                    res.append(node)
            if res:
                return res
            updated = set()
            queue = {s[:i] + s[i+1:] for s in queue for i in range(len(s))}
