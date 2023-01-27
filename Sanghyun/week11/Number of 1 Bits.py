class Solution:
    # 1비트가 몇개 있는지 반환 
    def hammingWeight(self, n: int) -> int:
        # 개수 저장 
        count = 0
        # n이 0이 아니면 반복 
        while n:
            # n-1과 n이랑 and조건으로 갱신 
            n &= n - 1
            # 1개수 갱신 
            count += 1
        # 비트에 몇개의 1이 있는지 반환 
        return count

        # 더 쉽게 풀려면 사용하면 됨 
        #return bin(n).count('1')