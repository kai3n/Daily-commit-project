def solution(citations):
    # 우선 논문들 피인용수 내림차순으로 정렬 
    citations.sort(reverse =True)
    # # H-index는 논문 수보다 피인용수가 많거나 같을때의 값이 H-index임
    for index , citation in enumerate(citations):
        # 논문수가 많거나 같을때 인용 회수 반환 
        if index >= citation:
            return index 
    # 인용횟수가 많다면 논문 수 반환 
    return len(citations)