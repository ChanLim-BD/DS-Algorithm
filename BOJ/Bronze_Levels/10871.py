import sys
n, x = map(int, sys.stdin.readline().split(" "))
a = list(map(int, sys.stdin.readline().split(" ")))

for i in a:
    if (i < x):
        print("%d" % i, end=' ')


"""
input()으로 값을 입력받아 list를 만드는 방법은

   - 데이터 값이 정수 일 경우: 리스트 이름 = list(map(int, input().split()))

   - 데이터 값이 문자 일 경우: 리스트 이름 = list(input().split())
"""
