class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid, res = len(s) // 2, 0
        for i in range(mid):
            if s[i] in vowels:
                res += 1
            if s[mid + i] in vowels:
                res -= 1
        return res == 0
