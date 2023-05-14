from collections import deque

def solution(maps):
    # x, y 길이 저장
    len_x,len_y = len(maps) , len(maps[0])
    # 초기 큐 값 설정
    queue = deque([(0,0)])
    # 상하좌우 이동할 값 저ㅇ
    direct = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while queue:
        # 기준 좌표 설정
        x,y = queue.popleft()
        # 상하좌우 값 갱신 
        for i in range(4):
            new_x = x + direct[i][0]
            new_y = y + direct[i][1]
            # 탐색하지 않은곳은 값 갱신 후 큐에 추가
            if 0 <= new_x < len_x and 0 <= new_y < len_y and maps[new_x][new_y] == 1 :
                maps[new_x][new_y] = maps[x][y] +1
                queue.append((new_x,new_y))
    # 도착 지점이 1보다 크면 그 값 반환
    if maps[-1][-1] > 1:
        return maps[-1][-1]
    # 도착 지점에 도착 못하면 -1 반환
    else:
        return -1