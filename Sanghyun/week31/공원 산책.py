def solution(park, routes):
    x = 0 
    y = 0
    # 시작점 찾기 
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x = j
                y = i
                break

    for route in routes:
        # 이동한 위치 값 저장
        new_x = x 
        new_y = y
        for item in range(int(route[2])):
            # 동쪽으로 이동할경우 
            if route[0] =='E' and new_x != len(park[0])-1 and park[new_y][new_x+1] !='X':
                new_x +=1
                if item == int(route[2])-1:
                    x = new_x
            # 서쪽으로 이동할경우
            elif route[0] =='W' and new_x != 0 and park[new_y][new_x-1] !='X':
                new_x -=1
                if item == int(route[2])-1:
                    x = new_x
            # 북쪽으로 이동할 경우
            elif route[0] =='N' and new_y != 0 and park[new_y-1][new_x] !='X':
                new_y -=1
                if item == int(route[2])-1:
                    y = new_y
            # 남쪽으로 이동할경우
            elif route[0] =='S' and new_y != len(park)-1 and park[new_y+1][new_x] !='X':
                new_y +=1
                if item == int(route[2])-1:
                    y = new_y
    # 다 이동했을때 최종위치 반환
    return [y,x]