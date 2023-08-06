class Solution:
    def finalString(self, s: str) -> str:
        res = []
        flip = False
        for c in s:
            if c == "i":
                flip = not flip
            else:
                if flip:
                    res = [c] + res
                else:
                    res = res + [c]
        return "".join(res) if not flip else "".join(res[::-1])
