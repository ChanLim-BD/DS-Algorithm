def count_pair(string):
    stack = []
    answer = 0
    for c in string:
        if c in "({[":
            stack.append(c)
        elif len(stack) == 0:
            continue
        elif c == ']' and stack[-1] == '[':
            answer += 1
            stack.pop(-1)
        elif c == '}' and stack[-1] == '{':
            answer += 1
            stack.pop(-1)
        elif c == ')' and stack[-1] == '(':
            answer += 1
            stack.pop(-1)
        else:
            stack = []
            continue
    return answer

print(count_pair("()({({[()]})})"))
        