def solution(s):
    answer = []
    words = s.split(" ")
    for word in words:
        w = ""
        for i in range(len(word)):
            if i % 2:
                w += word[i].lower()
            else:
                w += word[i].upper()
        answer.append(w)
    return ' '.join(answer)

def main():
    print(solution("try hello world"))


if __name__ == '__main__':
    main()