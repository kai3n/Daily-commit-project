class Solution:
    def sumPrefixScores(self, W: List[str]) -> List[int]:
        C = collections.defaultdict(int)
        for w in W:
            for i in range(len(w)):
                C[w[:i + 1]] += 1
                
        ans = []
        for w in W:
            curr = 0
            for i in range(len(w)):
                curr += C[w[:i + 1]]
            ans.append(curr)
            
        return ans
