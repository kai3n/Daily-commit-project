class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        for w in path.split('/'):
            if w == "..":
                if res:
                    res.pop()
            elif w not in ('', '.'):
                res.append(w)
        return "/" + "/".join(res)
