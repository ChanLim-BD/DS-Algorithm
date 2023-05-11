def solution(st):
    cases = []
    for i in range(65, 91):
        cases.append(chr(i))
    for i in range(97, 123):
        cases.append(chr(i))
    
    if len(st) == 4 or len(st) == 6:
        for s in cases:
            if s in st:
                return False
        return True
    else:
        return False

def alpha_string46(s):
    return s.isdigit() and len(s) in [4,6]