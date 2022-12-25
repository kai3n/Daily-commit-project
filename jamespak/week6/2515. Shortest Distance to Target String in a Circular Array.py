class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n = len(words)
        dist = float("inf")
        for i in range(n):
            c_dist = abs(i - startIndex)
            if words[i] == target:
                dist = min(dist, c_dist, n-c_dist)
        return dist
