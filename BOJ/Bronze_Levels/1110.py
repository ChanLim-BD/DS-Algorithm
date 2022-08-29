import sys
num = int(sys.stdin.readline())

start = num
count = 0

while(1):
    start = (start % 10)*10 + (start // 10 + start % 10) % 10
    count += 1
    if (num == start):
        break

print(count)


"""
26 -> 2+6=8, 68 -> 6+8=14, 84 -> 8+4=12, 42 -> 4+2=6, 26
8 -> 0+8=8, 88 -> 8+8=16, 86, -> 8+6=14, 64 -> 6+4=10, 40-> 4+0=4, 4-> 0+4=4, 44-> 4+4=8, 
"""
