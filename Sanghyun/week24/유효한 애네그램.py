class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 정렬 해서 같으면 True반환
        return sorted(s) == sorted(t)