import heapq

def solution(operations):
    # 결과값 저장
    answer = []
    # 큐 생성
    q = []
    for operation in operations:
        # 명령어 저장
        x, num = operation.split() 
        num = int(num)
        # x가 I가 나올때 q에 저장
        if x == 'I':
            heapq.heappush(q, num)
        # D, 1이 나오면 큐에서 최대값 삭제
        elif x == 'D' and num == 1:
            if len(q) != 0:
                max_value = max(q)
                q.remove(max_value)
        else:
            # 큐에서 최소값 제거
            if len(q) != 0:
                heapq.heappop(q)
    # 큐가 비어있으면 [0,0] 저장
    if len(q) == 0:
        answer = [0, 0]
    else:
        # 큐가 존재하면 [최대값,최소값] 저장
        answer = [max(q), heapq.heappop(q)]
    # 결과 반환
    return answer