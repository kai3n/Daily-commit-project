class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        d = defaultdict(int)
        for word in words:
            if d[word[::-1]] > 0:
                res += 1
                d[word[::-1]] -= 1
            else:
                d[word] += 1
        return res
