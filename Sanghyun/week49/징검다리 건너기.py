def solution(stones, k):
    # 이진 탐색으로 접근
    left, right = 1, max(stones)
    # 건널 사람 최소 1명이므로 초기화
    answer = 1
    while left <= right:
        # 건너는 친구 수
        mid = (left + right) // 2  
        # mid명 건넌다고 가정했을 때 연속 점프수가 k 초과 시 건너기 불가능하므로 break
        cnt = 0  
        for stone in stones:
            if stone - mid < 0:
                cnt += 1
                 # 건널 수 없으므로 건널 사람 줄이기
                if cnt >= k:
                    right = mid - 1 
                    break
            else:
                cnt = 0     
        # mid명 건널 수 있으므로 건널 사람 갱신
        else:  
            answer = mid
            left = mid + 1
    # 징검다리 몇명 건널수 있는지 반환
    return answer
