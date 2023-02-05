import collections

class Solution:
    # 키값이 없으면 에러 발생 처리를 위해서 collections으로 선언 
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        # dp[n] 값이 존재하면 그대로 반환 
        if self.dp[n]:
            return self.dp[n]
        # 위 경우 아니면 dp[n]에 값을 설정
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        # dp에서 해당 값 반환
        return self.dp[n]