def solution(n, t, m, p):
    # n진수로 변환하는 함수
    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
    # 튜브의 정답 저장
    answer = ''
    # 모든 정답 저장
    candidate = []

  # 모든 턴의 답
    for i in range(t*m):
        conv = convert(i, n)
        for c in conv:
            # 전환 후 크기가 1씩 다 저장
            candidate.append(c)

    # 튜브의 정답만 저장
    for i in range(p-1, t*m, m):
        answer += candidate[i]
    # 튜브 정답 반환
    return answer