import random as r

total_score = []
class_score = []
student_score = []

for i in range(7):
    class_score = []
    for i in range(30):
        student_score = []
        for i in range(5):
            student_score.append(r.randint(40, 100))
        class_score.append(student_score)
    total_score.append(class_score)
    
total_average = 0
c_average = []
s_average = 0
# print(sum(total_score)) #Error

for c in total_score:
    for s in c:
        s_average += sum(s)/5
    c_average.append(s_average // 30)
    s_average = 0

print(c_average)
print(sum(c_average)//len(c_average))