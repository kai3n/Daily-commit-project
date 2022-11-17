def solution(skill, skill_trees):
    # 가능한 스킬이 몇개 인지 저장
    answer = 0
    # 총 가지고 있는 스킬을 차례대로 불러옴 
    for item in skill_trees:
        # 선행되는 순서로 저장
        s = ''
        # 한개의 스킬을 배울 때 선행되야하는 것을 순서대로 확인 
        for c in item:
            # 스킬이 skill에 포함된다면 s에 차례대로 추가 
            if c in skill:
                s += c
        # 선행되어야 되는 스킬이 같다면 가능한 스킬트리 
        if skill[:len(s)] == s: 
            answer += 1
    # 가능한 스킬 갯수 출력 
    return answer