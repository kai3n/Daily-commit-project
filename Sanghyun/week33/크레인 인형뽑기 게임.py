def solution(board, moves):
    # 인형 뽑은거 저장
    store = []
    # 인형 사라진 갯수 저장
    answer = 0

    for move in moves:
        for item in board:
            # 0이 아니면 인형뽑음
            if item[move-1] !=0:
                store.append(item[move-1])
                # 인형 뽑고 0으로 변경
                item[move-1]=0
                break
        # 뽑은 후 쌓을때 이전과 인형이 동일하다면 두개 없애줌
        if len(store) >=2 and store[-1] == store[-2]:
            # 인형 사라진 갯수 갱신
            answer+=2
            store = store[:-2]
    # 몇개 인형이 사라졌는지 반환
    return answer