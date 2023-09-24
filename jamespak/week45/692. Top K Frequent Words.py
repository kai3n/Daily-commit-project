class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        res = sorted(d, key=lambda x: (-d[x], x))
        return res[:k]
