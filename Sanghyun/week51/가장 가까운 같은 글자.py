def solution(s):
    answer = []
    dic = dict()
    for i in range(len(s)):
        # dic에 없으면 answer에 -1추가
        if s[i] not in dic:
            answer.append(-1)
        # 같은 글자가 있으므로 지금 인덱스와 나왔던 인덱스 뺴서 저장
        else:
            answer.append(i - dic[s[i]])
        # 글자 위치 갱신
        dic[s[i]] = i
    # 자신과 가장 가까운 곳에 있는 같은 글자 위치 반환
    return answer