def solution(quiz):
    answer = []
    for i in quiz:
        # = 을 기준으로 뽑아서 eval함수로 식을 계산해서 비교 
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            #같으면 O 다른면 X반환
            answer.append('O')
        else:
            answer.append('X')
    #결과 반환
    return answer