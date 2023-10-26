def solution(s):
    # 중간값 저장
    num = int(len(s)/2)
    # 홀수이면 중간값 반환
    if len(s)%2==1:
        return s[num]
    # 짝수이면 중간값 2개 반환
    return s[num-1:num+1]