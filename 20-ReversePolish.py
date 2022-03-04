def evalRPN(tokens: list) -> int:
    stack = []
    ops = {'*', '/', '+', '-'}
    for token in tokens:
        if token in ops:
            b = stack.pop()
            a = stack.pop()     # We can be sure there will always be at least 2, since the expression is guaranteed to be valid
            # print(n)
            if token == '*':
                stack.append(a*b)
            elif token == '/':
                if (a < 0) ^ (b < 0):
                    stack.append(-(abs(a) // abs(b)))
                else:
                    stack.append(a//b)
            elif token == '+':
                stack.append(a+b)
            else:
                stack.append(a-b)
        else:
            stack.append(int(token))
        # print(stack)
    return stack[-1]


if __name__ == "__main__":
    print(evalRPN(["2", "1", "+", "3", "*"]))       # 9
    print(evalRPN(["4", "13", "5", "/", "+"]))       # 6
    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*",
                   "/", "*", "17", "+", "5", "+"]))      # 22
