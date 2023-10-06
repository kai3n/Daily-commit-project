class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1 
        carry = 0
        res = []

        while i >= 0 or j >= 0:
            n1 = n2 = 0
            if i >= 0:
                n1 = ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                n2 = ord(num2[j]) - ord('0')
                j -= 1
            t = n1 + n2 + carry
            res.append(t%10)
            carry = t//10
        if carry:
            res.append(carry)
        return ''.join(map(str, res))[::-1]
