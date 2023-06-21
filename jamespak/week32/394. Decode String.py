class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_string = ""
        
        for c in s:
            if c == "[":
                stack.append(cur_string)
                stack.append(cur_num)
                cur_num = 0
                cur_string = ""
            elif c == "]":
                n = stack.pop()
                s = stack.pop()
                cur_string = s + n * cur_string
                
            elif c.isdigit():
                cur_num = cur_num*10 + int(c)
            else: # a-z
                cur_string += c
        return cur_string
