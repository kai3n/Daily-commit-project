import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 돌 빈도수 계산
        freqs = collections.Counter(S) 
        # 보석이 계산
        count = 0

        # 빈도수 확인 후 count 갱신
        for char in J:
            count += freqs[char]
        # 보석이 몇개 있는 반환
        return count