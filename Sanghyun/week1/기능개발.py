def solution(progresses, speeds):
    # 몇개의 기능들이 끝낫는지 저장
    answer = []
    # progresses가 존재하면 계속 반복 
    while progresses: 
        # 현재 progresses에서 하루치 할당량 다 더해서 갱신 
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 몇개의 기능이 완성됬는지 저장 
        count = 0 
        # progress가 존재하고 100이상이면 작업이 끝낫으므로 progresses랑 하루 작업량 제거 
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            # 한개의 기능이 끝낫으므로 값을 갱싱 
            count +=1
        # 끝난  0보다 클 경우 answer에 저장 
        if count > 0 :
            answer.append(count)
    # 몇개의 기능이 끝낫는지 반환 
    return answer