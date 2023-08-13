def solution(dirs):
    # 경로 저장
    course = set()
    # y,x 초기 좌표 
    y, x = 0, 0
    # UDRL 좌표 이동
    table = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    
    for d in dirs:
        # dirs에 문자 하나마다 좌표 값 가지고옴
        dy, dx = table[d]
        # 새로운 좌표로 저장
        ny = y + dy
        nx = x + dx
        # 새로운 좌표가 좌표평면 경계안에서만 동작
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            # 출발지 좌표와 도착지 좌표 저장
            course.add(((y, x), (ny, nx)))
            # 도착지 좌표와 출발지 좌표 저장
            course.add(((ny, nx), (y, x)))
            # y,x 값 갱신
            y = ny
            x = nx
    # 출발지 좌표와 도착지 좌표 2개로 저장했으므로 2로 나눠서 반환
    return len(course) // 2