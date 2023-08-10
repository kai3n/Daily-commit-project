def solution(survey, choices):
    # mbti 유형 저장
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    mbti=''
    for s,c in zip(survey,choices):
        # c가 비동의 일때 앞에 인덱스에 점수부여
        if c<4:
            dic[s[0]] += 4-c
        # c가 동의 일때 뒤에 인덱스에 점수부여
        elif c>4:
            dic[s[1]] += c-4
    # 키 값 리스트로 변환
    keys = list(dic.keys())
    values = list(dic.values())
    # mbti 점수비교 후 유형저장
    for idx in range(0,len(keys),2):
        if values[idx]>= values[idx+1]:
            mbti += keys[idx]
        else:
            mbti +=keys[idx+1]
    # mbti 반환
    return mbti