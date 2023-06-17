def solution(keymap, targets):
    # 자판 담을 키 
    key = {}
    # 결과 저장
    answer = []
    # 키값을 최소 몇번 눌러야지 테이블에 다 저장
    for keys in keymap:
        for i, value in enumerate(keys):
            if value not in key:
                key[value] = i + 1
            else:
                key[value] = min(key[value],i+1)
    # target키 값을 key에서 찾아서 있으면 최소 값만큼 눌러야 되므로 count를 갱신
    for target in targets:
        count = 0
        for item in target:
            if item  in key:
                count += key[item]
            # key가 없으면 키패드로 문자를 만들수 없으므로 count를 -1로 갱신
            else:
                count = -1
                break
        # count 저장
        answer.append(count)
    # 키패드로 최소 몇번눌러야 하는지 결과 반환
    return answer