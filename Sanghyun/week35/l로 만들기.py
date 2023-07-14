def solution(myString):
    # 알파벳저장
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # l 인덱스 저장
    l_idx = alpha.index('l')
    for i in myString:
        # l보다 인덱스 작으면 i로 바꿈
        if alpha.index(i) <= l_idx:
            myString = myString.replace(i,'l')
    # i보다 먼저 나온 알파벳 전환 후 반환
    return myString