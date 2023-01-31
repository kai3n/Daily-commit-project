from typing import List 
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 아이들 쿠키 원하는 순서대로 정렬 
        g.sort()
        s.sort()
        # 인덱스 설정 
        child = cookie = 0
        # 아이들이나 쿠키 크기가 사이즈보다 작을때만 반복 
        while child < len(g) and cookie < len(s):
            # 아이들이 원하는 쿠키 이상일떄 다음아이로 넘어감 
            if s[cookie] >= g[child]:
                child+=1
            # 반복문 한번에 cookie 인덱스 갱신 
            cookie +=1
        # 몇명의 아이들이 원하는 쿠기 이상으로 받을수 있는지 반환 
        return child