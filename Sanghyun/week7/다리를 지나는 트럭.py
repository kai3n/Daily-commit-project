def solution(bridge_length, weight, truck_weights):
    # 트럭들이 몇초 걸리는지 저장
    answer = 0
    # 다리에 트럭은 초단위로 올라가므로 다리의 길이에 차가없을수도 잇으니깐 일단 초기에 0으로 다갱신
    bridge = [0] * bridge_length
    # 다리의 길이를 줄이면서 1초 단위 계산하기 위해서 반복
    while len(bridge):
        # 반복문 한번 돌때마다 1초씩 추가 
        answer += 1
        # 미리 트럭이 들어올것에 대비해서 맨앞 위치를 제거 
        bridge.pop(0)
        # trucks의 weights가 있으면 이동할 트럭이 있으므로 반복 
        if truck_weights:
            # 다리위에 트럭 weight값이랑 현재 트럭 weights값이랑 합쳐서 다리가 견딜수 있으면 다리에 추가
            if sum(bridge) + truck_weights[0] <= weight:
                # 트럭 무게만큼 다리에 추가
                bridge.append(truck_weights.pop(0))
            else:
                # 다리가 무게가 제한되있으므로 기다려야 되기때문에 0을 추가 초를 더 늘림
                bridge.append(0)
    # 트럭들이 다리를 건너는데 몇초가 걸리는지 반환 
    return answer