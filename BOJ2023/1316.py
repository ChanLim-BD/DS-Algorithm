n = int(input())
answer = 0
words = [input() for _ in range(n)]

for word in words:
    checker = list(''.join(set(word)))
    tmp = [word[0]]
    for c in word:
        if tmp[-1] == c:
            pass
        else:
            tmp.append(c)
    if sorted(checker) == sorted(tmp):
        answer += 1
        
print(answer)


'''
4
aba
abab
abcabc
a
'''