from collections import deque

def solution(begin, target, words):
    # words에 target값이 없으면 0반환
    if target not in words:  
        return 0

    q = deque()
    # 초기 큐에 시작값, 카운트값 push
    q.append([begin, 0])

    while q:
        # 큐에서 pop
        x, cnt = q.popleft()
        # x가 target일때 카운트 반환
        if x == target:
            return cnt # target값이 되면 cnt 출력

        for i in range(0, len(words)):
            # 단어차이 개수 저장
            diff = 0
            word = words[i]
            for j in range(len(x)):
                # 단어차이 개수 갱신
                if x[j] != word[j]:
                    diff += 1
            # 단어가 한개 차이나면 큐에 카운트+1해서 저장
            if diff == 1:
                q.append([word, cnt + 1])
    # target값이 있으나 변환될 수 없으면 0반환
    return 0 