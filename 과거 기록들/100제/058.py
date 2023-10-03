pay = int(input())

print(format(pay, ','))

# 재귀

pay1 = input()

def form(n):
    if len(n) <= 3:
        return n
    else:
        return form(n[:len(n)-3]) + ',' + n[len(n)-3:]


print(form(pay1))
