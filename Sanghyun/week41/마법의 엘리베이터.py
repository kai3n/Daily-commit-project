def solution(storey):
    answer = 0
    # 엘리베이터 0층 아니면 계속 반버복
    while storey:
        # 나머지 반환
        5
        remainder = storey % 10
        # 6 ~ 9 층 일때 
        if remainder > 5:
            # 마법의돌 10 -remainder만큼 사용 
            answer += (10 - remainder)
            # 엘리베이터 층수 10만큼 올림
            storey += 10
        # 0 ~ 4 층 일때 마법의돌 그 층 만큼만 사용
        elif remainder < 5:
            answer += remainder
        # 5 층 일때 
        else:
            # 다음 자릿값이 5이상이면 층수 10만큼 올림
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        # 10^n단위로 계속 갱신
        storey //= 10
    # 0층으로 가기위해서 몇개의 마법의 돌을 사용하는지 반환
    return answer