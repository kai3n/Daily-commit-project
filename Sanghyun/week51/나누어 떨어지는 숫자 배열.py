def solution(arr, divisor):
    # x가 divisor로 나누어 떨어지면 arr저장
    arr = [x for x in arr if x % divisor == 0]
    # 정렬
    arr.sort()
    # 나누어 떨어지는 수가있으면 리스트로 변환 아니면 -1 반환
    return arr if len(arr) != 0 else [-1]