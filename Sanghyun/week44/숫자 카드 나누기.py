from math import gcd

# 최대 공약수 구하는 함수  
def get_gcd(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd(g, arr[i])
    return g


def solution(arrayA, arrayB):
    answer = 0
    # a,b 배열에서 각자 최대공약수 저장
    a, b = get_gcd(arrayA), get_gcd(arrayB)
    
    # 배열 B에 있는게 a 최대공약수로 안 나눠지면 answer 갱신
    for i in arrayB:
        if i % a == 0:
            break
    else:
        answer = max(a, answer)
    # 배열 A에 있는게 b 최대공약수로 안 나눠지면 answer 개싱
    for i in arrayA:
        if i % b == 0:
            break
    else:
        answer = max(b, answer)
    # 해당조건에 해당하는 양의 정수 반환
    return answer