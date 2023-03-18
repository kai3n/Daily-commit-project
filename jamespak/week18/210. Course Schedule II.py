class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(numCourses):
            degree[i] += 0

        for p in prerequisites:
            degree[p[0]] += 1
            graph[p[1]].append(p[0])

        queue = [k for k, v in degree.items() if v == 0]
        res = []
        while queue:
            course = queue.pop(0)
            res.append(course)

            for adj in graph[course]:
                    degree[adj] -= 1
                    if degree[adj] == 0:
                        queue.append(adj)
        return res if len(res) == numCourses else []
