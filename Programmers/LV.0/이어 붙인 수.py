def solution(num_list):
    sol1 = ''
    sol2 = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            sol1 += str(num_list[i])
        else:
            sol2 += str(num_list[i])
    return int(sol1) + int(sol2)