class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        d = defaultdict(list)
        for dislike in dislikes:
            d[dislike[0]].append(dislike[1])
            d[dislike[1]].append(dislike[0])

        c = defaultdict(int)
        for p in d.keys():
            if c.get(p, -1) == -1:
                c[p] = 1
                queue = [p]
                while queue:
                    n = queue.pop(0)
                    for adj in d[n]:
                        if c.get(adj, -1) != -1:
                            if c[n] == c[adj]:
                                return False
                        else:
                            c[adj] = c[n] ^ 1  
                            queue.append(adj)
        return True
