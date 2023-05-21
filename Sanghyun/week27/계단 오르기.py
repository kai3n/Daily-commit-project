import collections
class Solution:
    # 에러 방지로 defaultdict선언
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        # 2보다 아래일경우 반환
        if n<=2:
            return n
        # 메모이제이션 사용 
        if self.dp[n]:
            return self.dp[n]
        # 값 갱신 후 몇가지 경로인지 반환
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        