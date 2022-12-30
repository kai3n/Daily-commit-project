from itertools import product
def solution(word):
    # 리스트에 모든 경우의 수 저장 
    answer = []
    # word 사전 저장 
    li = ['A', 'E', 'I', 'O', 'U']
    # word갯수만큼 반복
    for i in range(1,len(word)+1):
        # li에 있는걸 repeat 몇개 원소 기준인지 모든경우를 반환해서 반복 
        for per in product(li,repeat = i):
            # answer에 리스트를 변환시켜서 저장 
            answer.append(''.join(per))
    # answer 오름차순으로 정렬
    answer.sort()
    # 정렬한 후에 word를 찾아서 index확인후 +1 한 다음에 반환
    return answer.index(word)+1