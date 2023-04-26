from itertools import permutations


def solution(babbling):
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    word = []
    for i in range(1, len(speak)+1):  # 1 2 3 4
        for j in permutations(speak, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer


def solution(babbling):
    c = 0
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c
