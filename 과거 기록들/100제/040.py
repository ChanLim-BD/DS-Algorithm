제한무게 = float(input())
친구수 = int(input())
친구몸무게 = []
전체몸무게 = 0
제한수 = 0
비교 = True

for i in range(친구수):
    친구몸무게.append(float(input()))
    전체몸무게 += 친구몸무게[i]
    if 전체몸무게 > 제한무게:
        if 비교:
            비교 = False
            제한수 = i
if 제한수 == 0 and 친구몸무게[0] <= 제한무게:
    print(len(친구몸무게))
else:
    print(제한수)
