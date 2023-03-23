class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = {i: set() for i in range(n)}
        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
        stack = [0]
        visited = set()
        while stack:
            node = stack.pop()
            if node in visited:
                return False
            visited.add(node)
            for adj in d[node]:
                stack.append(adj)
                d[adj].remove(node)
            del d[node]
        return not d
