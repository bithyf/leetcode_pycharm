def minRemoveToMakeValid(s) -> str:
    s_list = list(s)
    stack = []
    invalid = []
    for i in range(len(s_list)):
        if s_list[i] == '(':
            stack.append(i)
        elif s_list[i] == ')':
            if len(stack) == 0:
                invalid.append(i)
            else:
                stack.pop()
    for i in stack[::-1]:
        del s_list[i]
    for i in invalid[::-1]:
        del s_list[i]
    return ''.join(s_list)
