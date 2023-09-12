def solution(chicken):
    answer = 0
    # 쿠폰 10개 이상일 때
    while chicken >= 10:
        # 몫과 나머지 구하기
        div, mod = divmod(chicken, 10)
        # 치킨서비스 받은 수 갱신
        answer += div
        # 목과 나머지 더해서 갱신
        chicken = div+mod
    # 몇마리 치킨 서비스 받는지 반환
    return answer