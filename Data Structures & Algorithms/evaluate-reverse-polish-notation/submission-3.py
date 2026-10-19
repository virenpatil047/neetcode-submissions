class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def calc(a, b, t):
            a = int(a)
            b = int(b)
            match t:
                case '+':
                    return a + b
                case '-':
                    return a - b
                case '*':
                    return a * b
                case '/':
                    return a / b

        res = []
        for e in tokens:
            if e not in ['+', '-', '*', '/']:
                res.append(e)
            else:
                c = calc(res[-2], res[-1], e)
                res.pop()
                res[-1] = c
        return int(res[-1])
                    