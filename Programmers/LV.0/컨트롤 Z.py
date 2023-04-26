def solution(s):
    numz = s.split()
    answer = []
    x = 0
    for n in numz:
        if n == "Z":
            answer.pop()
        else:
            answer.append(int(n))
    for i in answer:
        x += i
    return x
