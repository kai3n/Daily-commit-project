class Solution:
    def hammingWeight(self, n: int) -> int:
        # 2진법으롭 변환후 1개수 카운터 후 반환
        return bin(n).count('1')