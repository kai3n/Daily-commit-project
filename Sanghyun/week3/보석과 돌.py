import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 키값이 존재하지않으면 자동으로 값을 0으로 채워주는 dict선언 
        num = collections.defaultdict(int)
        # 몇개의 보석이 있는지 저장
        count = 0 
        # 돌에 들어잇는 보석들 빈도수를 저장
        for char in stones :
            num[char] +=1
        # 보석이 있으면 빈도수 만큼 반환해서 갱신 
        for char in jewels :
            count += num[char]
        # 돌에 들어 있는 보석이 몇개인지 반환 
        return count