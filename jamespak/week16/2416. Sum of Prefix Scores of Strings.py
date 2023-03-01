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
    
# Trie solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        node = self.trie
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.cnt += 1
            
    def count(self, word):
        node = self.trie
        ans = 0
        for ch in word:
            ans += node.children[ch].cnt
            node = node.children[ch]
        return ans

class Solution:
    def sumPrefixScores(self, A: List[str]) -> List[int]:
        trie = Trie()

        for a in A:
            trie.insert(a)

        return [trie.count(a) for a in A]
