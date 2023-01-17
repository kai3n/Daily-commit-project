class Solution:
    # 유효한 애너그램 판별 
    def isAnagram(self, s: str, t: str) -> bool:
        # 정렬해서 같으면 애너그램이므로 True 아니면 False 반환
        return sorted(s) == sorted(t)