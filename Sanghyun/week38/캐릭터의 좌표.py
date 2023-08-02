def solution(keyinput, board):
    # 가로 세로 최대값 설정
    x_lim,y_lim = board[0]//2,board[1]//2
    # 이동할 좌표
    move = {'left':(-1,0),'right':(1,0),'up':(0,1),'down':(0,-1)}
    # 초기 x,y 좌표
    x,y = 0,0
    
    for k in keyinput:
        # key값을 받아서 방향 저장
        dx,dy = move[k]
        # 최대값보다 크면 다시 key값을 받음
        if abs(x+dx)>x_lim or abs(y+dy)>y_lim:
            continue
        else:
            # x,y좌표 갱신
            x,y = x+dx,y+dy
    # 키 입력이 끝나고 캐릭터 좌표출력
    return [x,y]
