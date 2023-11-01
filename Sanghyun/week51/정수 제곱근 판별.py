def solution(n):
    # n이 양의 정수 x의 제곱 판단
    sqrt = n ** (1/2)
    # 1로 나눠지면 제곱이므로 +1 한후 제곱해서 반환
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    # 양의 정수 아니므로 -1반환
    return -1