def solution(price, money, count):
    # 산술 평균으로 부족한 금액반환
    return max(0,price*(count+1)*count//2-money)