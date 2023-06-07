import sys
X = int(sys.stdin.readline())

save = X
stick = 64
glue = 0
sum = 0

while (sum != save):
    while (stick > X):
        stick /= 2
    sum += stick
    X -= stick
    glue += 1
    stick = 64
print(glue)
