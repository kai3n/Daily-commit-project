from collections import deque

def solution(x, y, n):
    # 결과값 저장
    answer = -1
    
    q = deque()
    # 초기값 설정
    q.append((x, 0))
    # 탐색한곳 제외
    visited = set()
    
    while q:  
        # 큐에 있는 값 추출
        value, cnt = q.popleft()
        # 같으면 cnt 값 반환
        if value == y:
            answer = cnt
            break
        # value에 *3 한후 y보다 작으면 큐에 저장
        if value*3 <= y and not value*3 in visited:
            visited.add(value*3)
            q.append((value*3, cnt+1))
        # value *2 한후 y보다 작으면 큐에 저장
        if value*2 <= y and not value*2 in visited:
            visited.add(value*2)
            q.append((value*2, cnt+1))
            # value +n 한후 y보다 작으면 큐에 저장
        if value+n <= y and not value+n in visited:
            visited.add(value+n)
            q.append((value+n, cnt+1))
    # x에 *2,*3,+n을 몇번해야지 y값 만드는지 출력
    return answer