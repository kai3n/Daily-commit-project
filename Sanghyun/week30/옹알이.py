def solution(babbling):
    # 발음들 저장
    prons =['aya','ye','woo','ma']
    result = 0
    for item in babbling:
        for pron in prons:
            # 단어중 연속된 발음 제외하고 공백으로 대체
            if pron*2 not in item:
                item = item.replace(pron,' ')
        # 연속된 발음을 제외하고 발음을 다하면 공백이므로 result 갱신
        if item.isspace():
            result+=1
    # 단어들중 발음을 몇개 할수있는지 반환
    return result