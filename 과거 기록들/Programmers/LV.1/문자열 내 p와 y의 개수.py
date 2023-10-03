from collections import Counter

def solution(st):
    c = Counter(st)
    if c['p'] + c['P'] == c['y'] + c['Y']:
        return True
    else:
        return False
    
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')