class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(map(int, list(str(n)[::2]))) - sum(map(int, list(str(n)[1::2])))
