class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(str(num))
        return int("".join(num[::2])) + int("".join(num[1::2]))
