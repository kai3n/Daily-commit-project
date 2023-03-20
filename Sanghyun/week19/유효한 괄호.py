class Solution:
    def isValid(self, s: str) -> bool:
        # 스택 저장
        stack = []
        # 키 값으로 미리 테이블 설정 
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for char in s:
            # (, {, [ 값은 stack 추가 
            if char not in table:
                stack.append(char)
            # )값이 나왔는데 스택이 없거나 스택에 마지막이 (이 아니면 False
            elif not stack or table[char] != stack.pop():
                return False
        # stack이 비어있을때 True반환 아니면 False반환
        return len(stack) == 0