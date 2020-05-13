def scoreOfParentheses(S):
    stack = []
    for element in S:
        if element is '(':
            stack.append(element)
        else:
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                Sum = 0
                while stack[-1] != '(':
                    Sum += stack.pop()
                stack.pop()
                stack.append(Sum * 2)
    return sum(stack)