def solution(people, limit):
    # 몸무게 순서대로 정렬 
    people.sort()
    # 제일 작은 사람 인덱스는 left , 제일 많은 사람은 인덱스 right 
    left , right = 0 ,len(people) -1
    # 몇개의 구명보트가 필요한지 카운트 
    count = 0 
    # 구명 보트에 최대 2명 탈수 있으므로 인덱스가 같아 질때까지 반복 
    while left <= right :
        # 초기 left가 right 보다 작으면 구명보트는 한대는 무조건 필요하니깐 count값 갱신
        count +=1
        # left인덱스 인 사람 몸무게랑 right인덱스 인 사람 몸무게가 limit 보다 작으면 둘이 같이 보트에 탈수 있으므로 left값 변경 
        if people[left]+people[right] <=limit:
            left+=1 
        # limit 가 초과되므로 right 인덱스 하나 죽임 
        right-=1

    # 구명보트에 몇명 탈수있는지 반환 
    return count