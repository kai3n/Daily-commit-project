from itertools import permutations

def solution(numbers):
    # 소수 판별 함수 
    def isPrime(x):
        # 2보다작으면 소수가 아니므로 False 반환 
        if x<2:
            return False
        else:
            # 나눠서 떨어지면 소수가 아니므로 False반환 
            for i in range(2,x):
                if x % i == 0:
                    return False
            # 소수이므로 True반환 
            return True
    # 소수가 몇개 인지 개수 저장    
    count = 0
    # 순열 경우의 수 저장공간 
    store = []

    for i in range(1,len(numbers)+1):
        # numbers에서 i개를 기준으로 순열을 생성해서 리스트를 join으로 합쳐주고 set으로 중복을 제거후 리스트로 다시 변환
        case = list(set(map(''.join,permutations(numbers,i))))
        for value in case:
            # case있는 값들 다 저장
            store.append(int(value))
    # store에 01, 1 있는경우 같으므로 중복 제거 
    store = list(set(store))
    # store에 잇는 값들 소수판별해서 소수이면 count +1로 갱신 
    for value in store:
        if isPrime(value)== True:
            count +=1
    # numbers의 순열에서 소수몇개인지 반환
    return count