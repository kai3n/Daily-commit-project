def solution(score):
    # 등수 저장
    answer =[]
    # 각자 영어 수학 총합 저장
    total_score = [sum(i) for i in score] 
    # 전체 점수 높은 순으로 내림차순으로 저장
    sorted_total_score = sorted(total_score, reverse=True)
    # 같은 점수는 앞에 인덱스 추출해서 등수저장
    for i in total_score:
        answer.append(sorted_total_score.index(i)+1)
    # 반에서 등수 반환
    return answer