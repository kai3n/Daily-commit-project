def solution(routes):
    # 몇 대의 카메라를 설치해야 하는지 저장
    answer = 0
    # routes를 차량이 나간 기준으로 정렬 
    routes.sort(key=lambda x: x[1])
    # -30001부터 카메라 위치를 찾습니다.
    camera = -30001 
    
    for route in routes:
        # 차량이 진입할때 카메라 위치보다 크면 카메라 설치
        if camera < route[0]:
            answer += 1
            # 카메라 위치 갱신
            camera = route[1]
    # 몇 대 카메라 설치했는지 반환
    return answer