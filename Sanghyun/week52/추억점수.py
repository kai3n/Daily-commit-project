def solution(name, yearning, photo):
    table = {}
    for i in range(len(name)):
        # table에 사람이름을 키값으로 그리움값 저장
        table[name[i]] = yearning[i]

    answer = []

    for p in photo:
        # 추억점수 저장
        cnt = 0
        for a in p:
            if a in table:
                # table에 이름이 존재할시 추억점수 갱신
                cnt += table[a]
        answer.append(cnt)
    # 그리움 점수 반환
    return answer