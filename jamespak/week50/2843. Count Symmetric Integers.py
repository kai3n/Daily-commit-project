class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            if len(str(num))%2 == 0:
                a = str(num)[:len(str(num))//2]
                b = str(num)[len(str(num))//2:]
                if sum(int(n) for n in a) == sum(int(n) for n in b):
                    count += 1
        return count
