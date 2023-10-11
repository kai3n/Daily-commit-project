import heapq

def solution(N, road, K):

    def dijkstra(dist,adj):
        heap = []
        # 가중치, 노드 저장 
        heapq.heappush(heap,[0,1])
        while heap:
            cost, node = heapq.heappop(heap)
            for c, n in adj[node]:
                # 인접노드의 가중치보다 작으면 갱신 
                if cost + c < dist[n]:
                    dist[n] = cost + c
                    heapq.heappush(heap, [cost+c,n])
                    
    # 노드 1번 붘터 최소값 저장
    dist = [float('inf')] * (N+1)
    # 초기 자기자신과는 연결안되므로 0저장
    dist[1] = 0 
    # 인접 노드 저장
    adj = [[] for _ in range(N+1)]
    for r in road:
        # 양방향으로 인접노드, 가중치 저장
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    # 다익스트라 알고리즘 사용 
    dijkstra(dist,adj)
    return len([i for i in dist if i<=K])