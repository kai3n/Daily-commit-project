def solution(board):
    N = len(board)
    boom=[]
    count = 0
    # 지뢰 주변 8군데 탐색 위치값
    dx = [-1, 1, 0, 0, -1, -1, 1, 1] 
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 지뢰 설치 
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                boom.append((i,j)) 
                
    # 폭탄 설치 
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갱신한 값이 범위안에 들어가면 지회 주변 폭탄 설치
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] = 1

    # 폭탄이 설치되지 않은 곳만 카운팅
    for x in range(N):
        for y in range(N):
            #
            if board[x][y] == 0:
                count += 1
    # 폭탄이 설치되지 않은 곳 개수반환
    return count