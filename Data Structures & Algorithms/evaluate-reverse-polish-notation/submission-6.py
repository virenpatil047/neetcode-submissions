class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(a, b, t):
            match t:
                case '+':
                    return a + b
                case '-':
                    return a - b
                case '*':
                    return a * b
                case '/':
                    return int(a / b)

        res = []
        for e in tokens:
            if e not in ['+', '-', '*', '/']:
                res.append(int(e))
            else:
                res[-2] = calc(res[-2], res[-1], e)
                res.pop()
        return res[-1]
                    