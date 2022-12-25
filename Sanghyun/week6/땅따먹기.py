def solution(land):
    # dp 저장
    dp = land
    # 갱신 할 행 만큼 반복 첫행은 갱신안하므로 1행부터 반복
    for i in range(1,len(land)): 
        # 갱신해야 할 열 만큼 반복 
        for j in range(len(land[0])):
            # 해당 값 + 이전 행에 해당 열제외한것중 최대값을 계속 갱신시켜줌
            dp[i][j] += max(dp[i-1][:j] + dp[i-1][j+1:])
    # 마지막 행에서 최댓값 반환 
    return max(dp[len(dp)-1])