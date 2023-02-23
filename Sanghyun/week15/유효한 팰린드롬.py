class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 공백 특수문제 뺴고 제거할 공간
        new_s = []
        for item in s:
            # 알파벳과 숫자 판별
            if item.isalnum():
                # 소문자로 다 저장
                new_s.append(item.lower())
        while len(new_s)>1:
            # 양쪽에 꺼냈을 때 같지않으면 False 
            if new_s.pop(0) != new_s.pop():
                return False
        # while문 벗어나면 거꾸로 뒤집어도 같은 문자이므로 True반환
        return True