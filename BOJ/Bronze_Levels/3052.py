a = []

for i in range(10):
    b = int(input())
    a.append(b % 42)

print(len(set(a)))
