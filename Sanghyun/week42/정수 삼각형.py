def solution(triangle):
    # dp 테이블 초기화
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    # dp 초기값 설정
    dp[0][0] = triangle[0][0]
    
    for i in range(0, len(triangle) - 1):
        for j in range(len(triangle[i])):
             # 거쳐간 숫자 최대값으로 계속 갱신 
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
    # 맨마지막 최값 반환
    return max(dp[-1])