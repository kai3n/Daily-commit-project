class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        
        s = s + "$"
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        prev = stack.pop()
                        if prev < 0:
                            stack.append(int(math.ceil(float(prev)/num)))
                        else:
                            stack.append(int(prev/num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c
            return sum(stack)
        return helper([], 0)
