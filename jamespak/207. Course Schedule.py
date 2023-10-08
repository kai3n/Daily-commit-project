class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        in_degree = defaultdict(int)
        for x, y in prerequisites:
            g[y].append(x)
            in_degree[x] += 1
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        while queue:
            node = queue.popleft()
            for adj in g[node]:
                in_degree[adj] -= 1
                if in_degree[adj] == 0:
                    queue.append(adj)
        return not sum(in_degree.values())
