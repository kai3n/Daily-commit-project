def solution(wall):
    # 시작점 종료점 모아두기 
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            # 파일있는 곳은 위치 다 저장
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    # 최소인점은 시작점, 최댓값은 종료점 반환
    return [min(a), min(b), max(a) + 1, max(b) + 1]