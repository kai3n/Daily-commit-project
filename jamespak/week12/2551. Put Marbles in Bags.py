class Solution:
        def putMarbles(self, A: List[int], k: int) -> int:
            B = [A[i] + A[i + 1] for i in range(len(A) - 1)]
            return sum(nlargest(k - 1, B)) - sum(nsmallest(k - 1, B))
