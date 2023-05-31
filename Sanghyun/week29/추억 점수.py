def solution(name, yearning, photo):
    #결과 저장
    result = []
    # 두개 데이터 엮어서 딕셔너리로 저장
    information = dict(zip(name, yearning))
    for people in photo:
        # 점수 초기화 
        score = 0
        for person in people:
            # 딕셔너리안에 사람이 있으면 점수 갱신
            score += information.get(person, 0)
        # 점수 저장
        result.append(score)
    # 점수 결과 반환
    return result