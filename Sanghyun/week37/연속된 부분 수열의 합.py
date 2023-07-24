def solution(sequence, k):
    # 부분 연속해서 k값 만들수 있는 인덱스 반환
    answer = []
    # 이동할 포인트
    right = 0 
    # 부분 수열합
    sub_sum = 0
    for left in range(len(sequence)):
        # right가 sequence 길이보다 작고 sub_sum이 k보다 작으면 반복
        while right < len(sequence) and sub_sum < k :
            # sub_sum에 right값 넣어주면 right 포인트 갱신
            sub_sum +=  sequence[right]
            right +=1 
        # sub_sum이 k랑 같을경우
        if sub_sum == k:
            # answer이 없으면 left,right-1값 저장
            if not answer:
                answer = [left,right-1]
            # 있을경우 answer의 right -left값 이 right-left-1보다 크면 answer 갱신 
            else:
                answer = [left, right-1] if answer[1] - answer[0] > right - 1 - left else answer
        # sub_sum에서 값제거 
        sub_sum -= sequence[left]
    # 부분 연속해서 k값 만들수 있는 인덱스 반환
    return answer