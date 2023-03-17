class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                queue = [i]
                visited.add(i)

                while queue:
                    node = queue.pop(0)
                    for adj in g[node]:
                        if adj not in visited:
                            queue.append(adj)
                            visited.add(adj)
                ret += 1
        return ret
