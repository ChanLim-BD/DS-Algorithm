morse = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z'
}


def solution(letter):
    codes = list(letter.split(' '))
    # ['....', '.', '.-..', '.-..', '---']
    answer = ""
    for code in codes:
        answer += str(morse.get(code))
    return answer


def main():
    print(solution(".... . .-.. .-.. ---"))
    print(morse)


if __name__ == '__main__':
    main()
