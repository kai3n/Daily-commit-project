import math

def solution(n, k):
    answer = 0
    # 소수 구하는 함수 
    def is_prime(x):
        # 1은 소수가 아니므로 False반환 
        if x == 1:
            return False
        # 제곱급만큼 반복
        for i in range(2, int(math.sqrt(x)) + 1):
            # 0일때는 나눠지므로 소수가 아니므로 False반환
            if x % i == 0:
                return False
        # 자기자신으로만 나눠지므로 소수 
        return True
    # k진수로 변환
    def to_n(n, k):
        temp = ''
        # 
        while n > 0:
            # 몫과 나머지 반환 
            n, mod = divmod(n, k)
            # 나머지 저장 
            temp += str(mod)
        # 역순으로 반환 
        return temp[::-1]
    # k진수로 바꾼 후 역순으로 변화 해서 0을 기준으로 리스트로 변환
    target = to_n(n,k).split('0')
    # target수 만큼반복
    for item in target:
        # item이 비어 있거든 소수가 맞다면 소수 옆에 0이 있으므로 answer에 +1갱신
        if item!='' and is_prime(int(item)):
            answer+=1
    # 변환 다 한수 소수주위에 0이 잇는 갯수 반환 
    return answer