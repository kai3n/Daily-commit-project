class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(lambda: defaultdict(int))
        for road in roads:
            g[road[0]][road[1]] = road[2]
            g[road[1]][road[0]] = road[2]
        candidates = set()
        visited = set()
        queue = deque([1])
        
        while queue:
            node = queue.popleft()
            visited.add(node)

            for nei in g[node].keys():
                if nei not in visited:
                    candidates.add(g[node][nei])
                    queue.append(nei)
        return min(candidates)
