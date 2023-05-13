class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        v = Counter(arr).values()
        return True if len(v) == len(set(v)) else False
