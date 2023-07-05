class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for edge in edges:
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
        
        queue = [source]
        visited = set()
        visited.add(source)

        while queue:
            node = queue.pop(0)
            if node == destination:
                return True
            
            for adj in g[node]:
                if adj not in visited:
                    visited.add(adj)
                    queue.append(adj)
        return False
