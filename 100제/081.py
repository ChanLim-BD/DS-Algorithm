flag = []  # 지뢰 없이 깃발만 있는 리스트
minesweeper = []  # 지뢰를 찾은 리스트

for _ in range(5):
    flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))

for i in flag:
    for j in range(len(i)):
        if i[j] == '1':
            i[j] = 'f'

for i in flag:
    print(i)

count = 0
search = 0

minesweeper = flag.copy()

for s in minesweeper:
    for i in s:
        if i == 'f':
            search = s.index(i)
            if search > 0:
                s[search-1] = '*'
            if search < 4:
                s[search+1] = '*'
            if count > 0:
                minesweeper[count-1][search] = '*'
            if count < 4:
                minesweeper[count+1][search] = '*'

    count += 1

print()
for j in minesweeper:
    print(j)
