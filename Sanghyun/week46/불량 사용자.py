from itertools import permutations

def check(users, banned_id):
    for i in range(len(banned_id)):
        # 길이가 다르므로 False반환
        if len(users[i]) != len(banned_id[i]):
            return False
        # *이면 다 가능하므로 continue
        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            # 값이 다르므로 False반환
            if banned_id[i][j] != users[i][j]:
                return False
    # banned에 걸리므로 True반환
    return True

def solution(user_id, banned_id):
    # banned_id길이만큼 순열 저장
    user_permutation = list(permutations(user_id, len(banned_id)))
    # ban되는 아이디저장
    ban_set = []

    for users in user_permutation:
        # users 아이디 ban체크
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            # ban_set에 없으면 저장
            if users not in ban_set:
                ban_set.append(users)
    # ban되는 아이디 개수 반환
    return len(ban_set)