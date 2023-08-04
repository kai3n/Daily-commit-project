def solution(spell, dic):
    for i in dic:
        # spell이랑 dic의 item이 정렬해서 같으면 1반환
        if sorted(list(i)) == sorted(spell):
            return 1
    # 아닐경우 2반환
    return 2