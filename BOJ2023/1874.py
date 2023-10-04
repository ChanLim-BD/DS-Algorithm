'''
4 3 6 8 7 5 2 1

1 2 3 4
+ + + +
1 2 3                           4
        -
1 2                             4 3
          -
1 2 5 6                         4 3
            + +
1 2 5                           4 3 6
                - 
1 2 5 7 8                       4 3 6
                  + +
1 2 5 7                         4 3 6 8
                     -
1 2 5                           4 3 6 8 7
                       -
                                4 3 6 8 7 5 2 1
                         - - - 
'''

n = int(input())                         # 1 2 3 4 5 6 7 8 
stack, ans, find = [], [], True

now = 1

for _ in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        ans.append('+')
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        find = False

if not find:
    print('NO')
else:
    for i in ans:
        print(i)

