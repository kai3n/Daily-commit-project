def solution(A,B):
    # 누적으로 저장 
    answer = 0 
    # A는 내림차순으로 정렬 
    A.sort(reverse=True)
    # B는 오름차순으로 정렬 
    B.sort()
    # answer에 곱의 최솟값 누적으로 저장
    for i in range(len(A)):
        answer += (A[i] * B[i])
    # 두개의 배열 중 곱햇을떄 누적 최솟값 반환 
    return answer