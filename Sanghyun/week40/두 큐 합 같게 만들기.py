from collections import deque

def solution(queue1, queue2):
    # 몇번만에 양쪽 큐의 합이 같아지는지 저장
    answer=0
    # 시간초과를 위해서 deque로 선언 
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    # 탐색 최대 카운트
    max_count =len(queue1) * 4
    # queue1, queue1 의 합 
    sum_que1 = sum(queue1)
    sum_que2 = sum(queue2)
    while True:
        # sum_que1이 더 크다면 값을 뺴서 queue2에 추가 후 갱신 
        if sum_que1 > sum_que2:
            value = queue1.popleft()
            queue2.append(value)
            sum_que1-=value
            sum_que2+=value
            answer+=1
        # sum_que2가 더 크다면 값을 뺴서 queue1에 추가 후 갱신
        elif sum_que1<sum_que2:
            value = queue2.popleft()
            queue1.append(value)
            sum_que2-=value
            sum_que1+=value
            answer+=1
        # 같으면 종료 
        else:
            break
        # answer이 max_count랑 같으면 모든 경우 다 탐색했으므로 같아질수가 없으므로 -1반환
        if answer == max_count:
            answer = -1 
            break
    # 두 큐의 합이 몇번만에 같아지는지 반환
    return answer