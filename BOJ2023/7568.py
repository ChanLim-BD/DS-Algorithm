num_student = int(input())
student_list = [list(map(int, input().split())) for _ in range(num_student)]

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")

"""
5
55 185
58 183
88 186
60 175
46 155
"""