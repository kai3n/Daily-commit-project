class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        total = 0
        l = 0

        for r in range(len(s)):
            d[s[r]] += 1

            while d[s[r]] > 1:
                d[s[l]] -= 1
                l += 1
            total += r - l + 1
        return total
