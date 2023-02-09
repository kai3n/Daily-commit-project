def solution(s, skip, index):
    # 알파벳 미리 저장 
    alpha = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    ]
    # 암호화 값 저장 
    answer =''
    # skip에 있는 값들은 aplha에서 제거 
    for item in skip:
        alpha.remove(item)
    # 인덱스 값만큼 더해서 암호화 후 answer에 저장
    for i in s:
        answer += alpha[(alpha.index(i)+index)%len(alpha)]
    # 암호화된 문자열 반환 
    return answer