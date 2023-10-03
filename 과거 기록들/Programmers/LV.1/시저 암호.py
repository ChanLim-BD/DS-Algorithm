def solution(s, n):
    answer = ''
    for c in s:
        if 65 <= ord(c) <= 90: 
            if  90 < ord(c) + n:
                answer += chr(ord(c) - 26 + n)
            else:
                answer += chr(ord(c) + n)
        elif 97 <= ord(c) <= 122:
            if  122 < ord(c) + n:
                answer += chr(ord(c) - 26 + n)
            else:
                answer += chr(ord(c) + n)
        elif c == ' ':
            answer += ' '
    return answer

def main():
    print(solution("AB", 1))


if __name__ == '__main__':
    main()