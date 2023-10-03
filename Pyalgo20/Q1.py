text = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ',]

# ord() : 문자 -> 숫자
# chr() : 숫자 -> 문자

st = [chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]

print(''.join(st))