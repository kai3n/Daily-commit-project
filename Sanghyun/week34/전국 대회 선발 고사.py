def solution(rank, attendance):
    answer = 0
    # 3등까지 저장
    cnt = 0
    for i in range(1, len(rank) + 1):
        # 학생 번호 저장
        num = rank.index(i)
        # 참가한다면 등수대로 점수 계산
        if attendance[num]:
            answer += num * 100 ** (2 - cnt)
            # 3등까지 갱신
            cnt += 1
        if cnt == 3:
            break
    # 3등까지 등수대로 등번호 계산 후 반환
    return answer