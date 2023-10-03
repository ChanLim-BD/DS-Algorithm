menu = [int(input()) for _ in range(5)]
lst = []
for i in range(len(menu) - 2):
    lst.append(menu[i] + menu[3] - 50)
    lst.append(menu[i] + menu[4] - 50)
print(min(lst))