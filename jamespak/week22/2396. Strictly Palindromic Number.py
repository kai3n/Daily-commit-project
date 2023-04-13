class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n-1):
            rep = []
            k = n
            while k > 0:
                rep.append(k%b)
                k //= b
            if rep != rep[::-1]: return False
        return True
