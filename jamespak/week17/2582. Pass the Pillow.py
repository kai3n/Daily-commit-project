class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 0
        direction = 0
        while time != 0:
            if i == 0 or i == n - 1:
                direction ^=1 
            if direction == 1:
                i += 1
            else:
                i -= 1
            time -= 1
        return i + 1
