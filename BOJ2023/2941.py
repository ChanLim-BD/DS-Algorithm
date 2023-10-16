croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수, 크로아티아 알파벳을 만나면 '*'로 변환하여 글자 수 편하게 셀 수 있다.
    print(word)
print(len(word))