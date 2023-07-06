def solution(babbling):
    # 발음 할수있는거 개수저장
    answer=0
    for value in babbling:
        word = ''
        # 문자를 다 저장
        for i in value:
            word +=i
            # 발음 할수있는게 있으면 word 갱신
            if word in ['aya','ye','woo','ma']:
                word = ''
        # word가 0이면 다 발음 가능하므로 개수 갱신
        if len(word)==0:
            answer+=1
    # 발음 할수있는 개수 반환
    return answer