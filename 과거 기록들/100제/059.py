# line = input()

# while(1):
#     if len(line) > 50:
#         print('Under 50 ##')
#         line = input()
#     else:
#         break

# out = '='*50

# print(out.insert(line, (len(out)//2)))

user_input = input()
print("{0:=^50}".format(user_input))  # 중앙 정렬 ^, := 빈 공백 대체
