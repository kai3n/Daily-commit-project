def solution(n):
    # n값 k에 저장 
    k = n
    # n을 2진수로 변환
    n_bin = bin(n)[2:]
    # 2진수로 변환한 n의 1 갯수 
    n_num = n_bin.count('1')

    # n보다 큰 자연수 2진수로 변환했을떄 1 갯수가 같은 값 반환 
    while True:
        # n 값에서 계속 +1씩 올라감 
        k +=1
        # 2진수로 변환 
        k_bin = bin(k)[2:]
        # 2진수로 변환한 k의 1 갯수
        k_num = k_bin.count('1')
        # 만약 2진수로 변환한 k의 1갯수랑 n의 1갯수 가 같다면 반복문 break
        if n_num == k_num :
            break
    # n보다 크고, 이진수 변환시 1갯수가 같은 최소 자연수 반환 
    return k