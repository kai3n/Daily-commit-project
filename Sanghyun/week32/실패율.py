def solution(N, stages):
    # 결과저장
    answer = []
    # 스테이지 길이
    length = len(stages)
    for i in range(1,N+1):
        # 스테이지 통과 못한사람 저장
        count = stages.count(i)
        # 실패율 계산
        if length ==0:
            fail = 0
        else :
            fail = count / length
        # 스테이지 통과못한 사람만큼 길이 뺴줌
        length -=count 
        # 스테이지마다 실패율 저장
        answer.append((i,fail))
    # 실패율 순서대로 정렬 후 결과값 반환
    answer = sorted(answer,key = lambda x : x[1] , reverse=True)
    return [i[0] for i in answer]