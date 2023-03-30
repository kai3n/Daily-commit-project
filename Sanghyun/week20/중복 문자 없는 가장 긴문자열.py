class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 사용한 키 값 저장
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자면 start 포인트 갱신 
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:  
                # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start + 1)

            # 현재 문자 인덱스 저장
            used[char] = index
        #최대 부분 문자열 길이 반환
        return max_length