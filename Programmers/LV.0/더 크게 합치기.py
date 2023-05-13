def solution(a, b):
    al = list(str(a))
    alc = al.copy()
    bl = list(str(b))
    blc = bl.copy()
    al.extend(blc)
    bl.extend(alc)
    x = int(''.join(al))
    y = int(''.join(bl))
    if x > y:
        return x
    else:
        return y

def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))