class Solution:
    # 두 정수를 입력받아 몇 비트가 다른지 계산
    def hammingDistance(self, x: int, y: int) -> int:
        # x y 를 2진수로 바꾸고 XOR로 한다음에 다를경우 1이 반환되므로 count함수로 1개수를 반환하면됨
        return bin(x^y).count('1')