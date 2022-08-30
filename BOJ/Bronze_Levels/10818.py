import sys
num = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
print(min(l))
print(max(l))


"""
python에선 리스트(배열)의 개수를 따로 설정할 필요가 없다.
동적으로 하니씩 추가할 때 마다 자동으로 공간이 할당되기 때문이다.
"""
