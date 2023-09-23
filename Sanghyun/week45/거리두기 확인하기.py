from collections import deque

def solution(places):
    
    def bfs(p):
        # P 위치 값들 저장
        starts = []
        for i in range(5):
            for j in range(5):
                if p[i][j] =='P':
                    starts.append([i,j])

        # P 위치값들 기준으로 탐색시작 
        for start in starts:
            queue = deque([start])
            # 방문했는지 체크
            visited = [[0]*5 for i in range(5)]
            # 경로 2이하 체크
            distance = [[0]*5 for i in range(5)]
            # 초기 탐색할때 방문했으므로 1로 변경
            visited[start[0]][start[1]] = 1
            
            while queue:
                # 좌표값 추출
                y,x = queue.popleft()
                # 상하 좌우로 이동
                dx = [-1, 1, 0, 0] 
                dy = [0, 0, -1, 1] 

                for i in range(4):
                    # y ,x 값 이동 후 갱신 
                    nx = x + dx[i]
                    ny = y + dy[i]
                    # 방문안하고 범위안에 있을때만 탐색
                    if 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0:
                        # 빈자리이므로 탐색후 방문 여부, 경로 길이 갱신
                        if p[ny][nx] == 'O':
                            queue.append([ny, nx])
                            visited[ny][nx] = 1
                            distance[ny][nx] = distance[y][x] + 1
                        # 거리가 1이하 이거나 탐색에 P가 존재할 경우 거리두기 실패이므로 0 반환
                        if p[ny][nx] == 'P' and distance[y][x] <= 1:
                            return 0
        # 거리두기 성공이므로 1반환
        return 1
    # 거리두기 성공 실패 여부저장 
    answer = []
    # 대기실 탐색
    for place in places:
        answer.append(bfs(place))
        
    return answer