class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # xor로 연산후 1개수 반환
        return bin(x^y).count('1')