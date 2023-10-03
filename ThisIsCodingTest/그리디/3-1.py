N = int(input())
count = 0

types = [500, 100, 50, 10]

for i in types:
    if N // i:
        count += N // i
        N = N % i

# if N // 500:
#     count += N // 500
#     N = N % 500
    
# if N // 100:
#     count += N // 100
#     N = N % 100
    
# if N // 50:
#     count += N // 50
#     N = N % 50
    
# if N // 10:
#     count += N // 10
#     N = N % 10

print(count)