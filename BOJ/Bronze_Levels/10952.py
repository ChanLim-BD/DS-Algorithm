import sys

while(1):
    try:
        a, b = map(int, sys.stdin.readline().split(" "))
    except:
        break
    print(a+b)

"""
 try 구문에는 에러가 발생할 여지가 있는 문장을 작성하고, except 구문에는 에러가 발생 시 실행시킬 문장을 작성한다.


"공백이 왜 오류야?"라고 생각할 수 있는데 input() 함수 입장에서 보면 아무것도 입력이 되지 않은 것이 오류라고 판단하게 되는 것이다.

 try - except - else - finally 구문도 있다. 
 else는 에러가 발생하지 않을 때 실행할 문장, finally에선 무조건 실행 할 문장으로 코드를 구현할 수도 있다.
"""
