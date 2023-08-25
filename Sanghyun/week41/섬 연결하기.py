def solution(n, costs):
    answer = 0
    # 비용기준으로 정렬
    costs.sort(key = lambda x: x[2]) 
    # 시작점 저장
    link = set([costs[0][0]])

    # 모든 위치가 연결될떄까지 반복
    while len(link) != n:
        for v in costs:
            # 두 섬이 연결 되어있으면 진행
            if v[0] in link and v[1] in link:
                continue
            # 두 섬이 연결 안되어있으면 link에 추가하고 비용추가
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break
    # 최소 비용 반환
    return answer
