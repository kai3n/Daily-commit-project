def solution(A, B):
    # 투포인트 사용 
    a_point , b_point = 0,0
    # B 승점 저장
    answer = 0
    # A,B 정렬
    A.sort()
    B.sort()

    while a_point != len(A) and b_point != len(B):
        # B가 크면 포인트들 다 갱신 및 B 승점 갱신
        if B[b_point] > A[a_point]:
            answer +=1
            a_point+=1
            b_point+=1
        else:
            # A가 크면 B포인트만 갱신
            b_point+=1
    # B 승점 반환 #수정
    return answer