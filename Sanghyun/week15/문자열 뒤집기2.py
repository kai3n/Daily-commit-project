from typing import List
class Solution:
    # 문자열 뒤집기 
    def reverseString(self, s: List[str]) -> None:
        # 투포인트 사용
        left, right = 0, len(s) - 1
        while left < right:
            # 좌우 값변경
            s[left], s[right] = s[right], s[left]
            # 인덱스 갱신
            left += 1
            right -= 1