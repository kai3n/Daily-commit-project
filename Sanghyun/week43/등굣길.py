def solution(m, n, puddles):
    # dp 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)] 
    # dp 초기값 설정
    dp[1][1] = 1
    
    # 물에 잠긴 곳은 -1로 표시
    for i, j in puddles: 
        dp[j][i] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1: 
                # 물에 잠겼으면 이후 값에 영향을 주지 않기 위해서 0으로 갱신
                dp[i][j] = 0 
                continue 
                
            # 위와 왼쪽에서 오는 경우 더해서 갱신
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    # 집에서 학교까지 물에 잠기지 않은 곳을 통해 올수있는 최단 경로 반환
    return(dp[n][m])