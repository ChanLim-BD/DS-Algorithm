student = ['강은지', '김유정', '박현서', '최성훈', '홍유진',
           '박지호', '권윤일', '김채리', '한지호', '김진이', '김민호', '강채연']


lst = list(enumerate(sorted(student), 1))

for i in lst:
    print('번호: {}, 이름: {}'.format(i[0], i[1]))
