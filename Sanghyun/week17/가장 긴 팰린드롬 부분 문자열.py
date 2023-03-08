class Solution:
    # 가장 긴 팰린드롬 반환
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left: int, right: int) -> str:
            # 팰린드롬 확인 후 투포인트로 양쪽으로 확장
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        
        # 최대 팰린드롬 판별해서 저장
        result = ""

        # 단어가 한개이거나 뒤집었을 때 같으면 반환
        if len(s) < 2 or s == s[::-1]:
            return s

        for i in range(len(s) - 1):
            # 2칸 3칸으로 한칸씩 이동하면서 팰린드롬 확인후 제일 긴 팰린드롬 저장
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        # 가장 긴 팰린드롬 반환
        return result