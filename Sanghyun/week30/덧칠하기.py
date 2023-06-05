from collections import deque

def solution(n, m, section):
    # 몇번의 페인트 칠하는지 저장
    answer = 0 
    # 페인트 안 칠해져있는곳 deque로 정의 
    queue  = deque(section)

    while queue:
        # 페인트 칠해야하는 부분 반환
        start = queue.popleft()
        # start+m 보다 queue[0]가 작으면 페인트 하나로 다 칠할수 있음
        while queue and start + m > queue[0]:
            queue.popleft()
        # 페인트 칠하는 개수 갱신
        answer+=1
    # 몇번 페인트 칠하는지 반환
    return answer