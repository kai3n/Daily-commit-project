def solution(n):
    # 점화식으로 접근 
    # n길이만큼 0으로 초기화 
    dp = [0 for i in range(n)]
    # 1,2는 바로 할당 
    dp[0], dp[1] = 1, 2
    # 인덱스 0, 1 을 제외하고 인덱스 2부터 갱신 
    for i in range(2, n):
        # 조건에서 경우의 수가 너무 많을경우 % 1000000007 나눠서 결과 반환
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    # 직 사격형을 채우는 방법의 수 반환 
    return dp[n-1]