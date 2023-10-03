def solution(age):
    st = str(age)
    ls = []
    for s in st:
        ls.append(int(s))
    for id, c in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 0):
        for i in range(len(ls)):
            if ls[i] == id:
                ls[i] = c
    ans = ''.join(ls)
    return ans


def solution1(age):
    conv = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
            '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    return ''.join(conv[i] for i in str(age))


def main():
    print(solution(23))


if __name__ == '__main__':
    main()
