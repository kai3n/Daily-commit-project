def solution(n, words):
    # 몇번 사람, 몇번째 차례인지 저장 
    answer = []
    # 단어의 길이는 2이상 이므로 1부터 단어갯수만큼 반복
    for i in range(1,len(words)):
        # 이전에 말햇던 단어가 있거나 tank -> wheel 처럼 앞단어 마지막이랑 뒷단어 처음 단어가 다르면 몇번째 사람인지 몇번째 차례인지 리스트에 저장
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            # index가 1부터 시작하므로 +1을 해서 리스트에 저장
            answer.append((i%n)+1)
            # 몇번째 차례인지 +1해서 리스트에 저장 
            answer.append((i//n)+1)
            return answer 
    # for문에서 return이 안되면 끝말잇기 잘된 경우 이므로 0,0반환 
    answer += [0,0]
    return answer