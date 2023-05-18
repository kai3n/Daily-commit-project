from typing import List 
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 오름차순으로 정렬 
        g.sort()
        s.sort()
        # 아이, 쿠키 포인트 초기화 
        child = cookie = 0

        while child < len(g) and cookie < len(s):
            # 아이가 원하는 것 보다 쿠키가 많으면 만족하므로 child 포인트 갱신 
            if s[cookie] >= g[child]:
                child+=1
            # 쿠키 포읹트 갱신
            cookie +=1
        # 몇명이 부여 받을수 있는지 반환
        return child