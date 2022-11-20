class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0

        g = defaultdict(list)
        for road in roads:
            g[road[0]].append(road[1])
            g[road[1]].append(road[0])
        
        def dfs(source, destination):
            people, liters = 1, 0

            for neibor in g[source]:
                if neibor == destination:
                    continue
                p, l = dfs(neibor, source)
                people += p
                liters += l
            liters += (people - 1) // seats + 1
            return people, liters
        
        return sum(dfs(n, 0)[1] for n in g[0])
