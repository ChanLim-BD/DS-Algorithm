def solution(my_string, letter):
    answer = ""
    for s in my_string:
        if s == letter:
            pass
        else:
            answer += s
    return answer


def solution1(my_string, letter):
    return my_string.replace(letter, '')
