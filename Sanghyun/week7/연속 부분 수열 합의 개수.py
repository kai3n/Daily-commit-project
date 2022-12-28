def solution(elements):
    # 연속 부분 수열이 몇개 인지 반환 
    answer = 0
    # 중복 제거 벼누 
    number_set = set()
    # 원형 수열이므로 연결되도록 할려면 2를 곱해서 값들 더하기 위함
    elements_double = elements * 2
    
    # elements 크기만큼 반복
    for i in range(len(elements)) : 
        # elements 크기만큼 반복
        for j in range(len(elements)) : 
            # 1개부터 5개까지 연속해서 number_set에 중복 제거 한 상태로 다 저장  
            number_set.add(sum(elements_double[j:j+i+1]))
    # number_set 개수는 연속 부분 수열의 합 결과값
    answer = len(number_set)
    # 연속 부분 수열의 합이 몇개인지 반환 
    return answer