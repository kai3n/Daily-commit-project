def solution(n, edge):
    # 인접 노드 초기화
    adj = [[] for _ in range(n + 1)]
    # 연결된 너무 다 저장
    for v1, v2 in edge:
        adj[v1].append(v2)
        adj[v2].append(v1)
    # 노드 방문체크 후 몇칸 떨어져 있는지 담기 위해서 초기화
    ch = [0 for _ in range(n + 1)]
    ch[1] = 1
    # 1번 노드부터 시작하므로 1저장
    queue = [1]
    
    while queue:
        # 현재노드 인덱스 반환
        cur = queue.pop(0)
        # 현재노드와 연결되어 있는 노드 다 탐색
        for dest in adj[cur]:
            # 탐색 안했던 노드면 탐색후 ch값 갱신
            if not ch[dest]:
                ch[dest] = ch[cur] + 1
                queue.append(dest)
    # 제일 먼 거리에 있는 노드가 몇개인지 반환
    return ch.count(max(ch))