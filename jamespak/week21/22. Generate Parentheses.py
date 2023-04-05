class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens):
            if left:
                generate(p + '(', left-1, right,parens)
            if right > left:
                generate(p + ')', left, right-1,parens)
            if not right:
                parens.append(p)
            return parens
        return generate('', n, n, [])
