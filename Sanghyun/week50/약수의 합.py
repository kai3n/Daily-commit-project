def solution(num):
    # num / 2 의 수들만 검사하고 num 더해주면 성능 더 좋아짐
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])