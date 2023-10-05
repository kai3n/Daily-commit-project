from collections import deque

def solution(m, n, board):
    answer = 0
    check_set = set()
    # board 초기화
    board = [list(i) for i in board]

    def check(b):
        for i in range(m-1):
            for j in range(n-1):
                # 2x2 블록 조건에 맞으면 집합에 해당 인덱스를 추가하는 함수
                if b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1] != '0':
                    check_set.add((i,j))
                    check_set.add((i+1,j))
                    check_set.add((i,j+1))
                    check_set.add((i+1,j+1))

    # board 2x2 있을때 재배치 
    def arrange(board):
        for j in range(len(board[0])):
            q = deque([])

            for i in range(len(board)-1,-1,-1):
                # 2x2해서 0으로 바꼇으면 q에 인덱스 저장
                if board[i][j] == '0':
                    q.append((i,j)) 
                else:
                    if q:
                        # 큐가 있으면 값 변경
                        qi, qj  = q.popleft()
                        board[qi][qj] = board[i][j]
                        board[i][j] = '0'
                        q.append((i, j)) 

    while True:
        # 2x2 블록 찾기
        check(board)
        if check_set:
            # board에 인덱스 갱신
            for i, j in check_set:
                board[i][j] = '0'
            # 없어진 블록 갯수 저장
            answer += len(check_set)
            # 없어진후 배열 재배치 
            arrange(board)
            # set 다 비움
            check_set.clear()
        else:
            break
    # 몇개의 블록이 사라졌는지 반환
    return answer