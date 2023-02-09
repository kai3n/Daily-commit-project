def solution(t, p):
    # 몇개인지 저장 
    answer = 0 
    # 부분문자열 다 뽑아낼수 있도록 반복 
    for i in range(len(t)-len(p)+1):
        # p의 크기만큼 t에서 뽑아서 item에 저장
        item = t[i:i+len(p)]
        # item이 p보다 작으면 answer값 갱신
        if item <= p:
            answer+=1
    return answer