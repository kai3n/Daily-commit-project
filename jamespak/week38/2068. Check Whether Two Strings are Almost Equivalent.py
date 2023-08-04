class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d = Counter(word1)
        for word in word2:
            d[word] -= 1
        return max(abs(val) for val in d.values()) <= 3
