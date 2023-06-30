def solution(num, total):
    # 값 평균 구하기 
    avg = total // num
    # num 개수로 연속된 수들을 더해서 total값 만드는 수들 반환
    return [i for i in range(avg - (num-1)//2, avg + (num+2)//2)]