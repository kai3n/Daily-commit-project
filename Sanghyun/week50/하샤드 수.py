def solution(n):
    # x 자릿수 합으로 x가 나눠지면 True 반환 아니면 False반환
    return n%sum(int(x) for x in str(n)) == 0