'''
1   0666
2   1666
3   2666
4   3666
5   4666
6   5666
7   6660
8   6661
9   6662
10  6663
11  6664
12  6665
13  6666
14  6667
15  6668
16  6669
17  7666
18  8666
19  9666
20  10666
21  11666
    12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
'''

n = int(input())

name = 666
cnt = 0

while(True):
    if "666" in str(name): 
        cnt += 1
        if cnt == n: 
            print(name)
            break
    name += 1