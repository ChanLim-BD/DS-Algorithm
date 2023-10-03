import sys
input = sys.stdin.readline

N = int(input())
people = []

for _ in range(N):
    old, name = input().split()
    people.append([int(old), name])
people.sort(key=lambda x:x[0])

for i in range(len(people)):
    print(people[i][0], people[i][1])
    