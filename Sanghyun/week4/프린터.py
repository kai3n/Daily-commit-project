def solution(priorities, location):
    # 중요도와 index 출력후 튜플형태로 저장 
    priorities = [(v, i) for i, v in enumerate(priorities)]
    # 몇번쨰로 인쇄되는지 카운트 
    count = 0

    while True:
        # 맨 처음 중요도가 priorities의 중요랑 같으면 count 갱신 
        if priorities[0][0] == max(priorities)[0]:
            count += 1
            # location과 index가 같으면 반복 중단 
            if priorities[0][1] == location:
                break
            # 위 조건에 안걸리면 해당 중요도 pop으로 제거 
            priorities.pop(0)
        # 같지 않으면 맨뒤로 보내기 
        else:
            priorities.append(priorities.pop(0))
    # 몇번째로 인쇄되는지 반환
    return count