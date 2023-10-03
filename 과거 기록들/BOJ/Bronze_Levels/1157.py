st = input().upper()
kind = sorted(list(set(st)))
count = []

for t in kind:
    count.append(st.count(t))

if count.count(max(count)) >= 2:
    print('?')
else:
    print(kind[count.index(max(count))])