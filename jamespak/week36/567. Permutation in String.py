class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in c:
                c[s2[i]] -= 1
            if i >= len(s1) and s2[i - len(s1)] in c:
                c[s2[i - len(s1)]] += 1
            
            if all(c[k] == 0 for k in c.keys()):
                return True
        return False
