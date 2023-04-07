import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 에러 방지 
        graph = collections.defaultdict(list)

        # # 키 값으로 그래프 뒤집어서 저장
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        # 여행일정 저장
        route = []

        def dfs(a):
            # 마지막값 출력 후 다시 탐색
            while graph[a]:
                dfs(graph[a].pop())
            # 탐색 한 대로 route에 추가
            route.append(a)

        dfs('JFK')
        # 결과 뒤집어서 반환
        return route[::-1]