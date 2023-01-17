# name = list(input().split())
# score = list(map(int, input().split()))

name = ['손오공', '야모챠', '메지터', '비콜로']
score = [70, 10, 55, 40]


def sol(name, point):
    d = {}
    z = [[i, j] for i, j in zip(name, point)]
    z = sorted(z, key=lambda x: x[1], reverse=True)

    for i in range(len(z)):
        d[z[i][0]] = i+1
    return d


print(sol(name, score))

