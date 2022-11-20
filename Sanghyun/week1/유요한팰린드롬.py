class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문자만 저장 리스트 
        str = [] 
        for char in s :
            # 만약에 문자이면 str에 소문자로 추가 
            if char.isalnum():
                str.append(char.lower())
        # str에 1개 이상존재하면 계속 반복 
        while len(str)>1:
            # str 맨앞 문자랑 맨뒤 문자가 같지 않으면 False 리턴 
            if str.pop()!=str.pop(0):
                return False
        # str이 0,1이면 뒤집어도 똑같은 말이 되기 때문에 True 반환
        return True