def solution(gems):
    answer = [0, len(gems)]
    # 보석 갯수
    gems_cnt = len(set(gems)) 
    # left는 보석 빼 줄 포인터, right는 보석 더해 줄 포인터
    left, right = 0, 0 
    # 초기 보석 저장 
    gem_dict = {gems[0] : 1}

    # 범위 벗어나면 종료 
    while left < len(gems) and right < len(gems):   
        # 딕셔너리에 보석 종류가 다 들어오는 경우
        if len(gem_dict) == gems_cnt:
            # right, left가 더 작아지면 answer 갱싱
            if right - left < answer[1] - answer[0]:
                answer = [left, right]       
            else:
                # 보석을 뺀 후 left 갱신 
                gem_dict[gems[left]] -= 1
                 # count가 0이 되면 key가 없어야하므로 del로 제외
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]   
                left += 1
        # 보석 종류가 다 없으면 right 포인터 갱신
        else:
            right += 1
            # right포인터가 끝까지 가면 탈출
            if right == len(gems):
                break
            # 딕셔너리 key에 있으면 count
            if gems[right] in gem_dict: 
                gem_dict[gems[right]] += 1
            else:
                gem_dict[gems[right]] = 1
    # 시작 인덱스가 1번 진열대 부터 라서 1 증가
    return [answer[0]+1, answer[1]+1] 