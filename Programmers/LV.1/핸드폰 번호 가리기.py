def solution(phone_number):
    ans = ''
    ans = ans + '*' * (len(phone_number) - 4)
    for i in range(len(phone_number) - 4, len(phone_number)):
        ans += phone_number[i]
    return ans


def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]