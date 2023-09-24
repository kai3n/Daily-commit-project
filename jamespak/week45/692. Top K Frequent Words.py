class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        h = [(-val, key) for key, val in d.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
