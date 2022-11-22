
from itertools import permutations

def solution(k, dungeons):
    # max값 저장
    max_value = 0
    # permutations은 수열로 dungeons 리스트를 , 갯수로 수열로 바꿔줌 
    for perm in permutations(dungeons, len(dungeons)):
        # 초기 피로도 저장 
        stamina = k 
        # 몇개 던전을 통과하는지 저장 
        cnt = 0
        # 수열에서 리스트 값들 반복 
        for item in perm:
            # 입장 피로도가 stamina보다 작을때 입장 할수 있음 
            if item[0] <= stamina:
                # 입장 후 피로도 소모 
                stamina = stamina - item[1]
                # 한개의 던전을 통과 했으므로 cnt값 갱신 
                cnt +=1
        # 수열중 최대 던전을 통과할수 있는 갯수 갱신 
        max_value = max(cnt,max_value)
    # 최대 던전 통과 갯수 반환 
    return max_value