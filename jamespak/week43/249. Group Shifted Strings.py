class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        g = collections.defaultdict(list)
        for s in strings:
            pattern = ()
            for i in range(1,len(s)):
                pattern += ((ord(s[i]) - ord(s[i-1]) + 26 ) % 26),
            g[pattern].append(s)
        return g.values()
