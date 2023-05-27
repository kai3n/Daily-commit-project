class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                s[i] = min(s[i], s[j])
                s[j] = min(s[i], s[j])
            i += 1
            j -= 1
        return "".join(s)
