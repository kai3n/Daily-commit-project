def solution(A, B):
    # 카운터 계산
    cnt = 0 
    for _ in range(len(A)):
        # A 랑 B 같으면 cnt 카운터 반환
        if A == B:
            return cnt
        # 문자열 한칸씩 오른쪽으로 밀어서 카운터 증가
        A = A[-1] + A[:len(A)-1]
        cnt +=1
    #  A를 밀어서 B를 못만들면 -1 반환
    return -1