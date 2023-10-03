def solution(sides):
    sides.sort(reverse=True)
    if sides[1] + sides[2] > sides[0]:
        return 1
    else:
        return 2
