"""
재귀함수

반복문을 재귀함수로 대체할 것이다.
"""

def greeting(count):
    

    if count == 99:
        return
    print(count)
    greeting(count+1)

greeting(1)
