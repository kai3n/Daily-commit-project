def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    # 0 개수 확인
    cnt_0 = lottos.count(0)
    # 로또 몇개 맞는지 확인
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    # 0이랑 맞는 개수가 최대 등수 , 맞는 개수는 최소 등수 반환
    return rank[cnt_0 + ans],rank[ans]