from collections import deque

"""
Queue를 구현할 때 주로 사용한다.
append, popleft

Stack은 그냥 리스트로
"""

dq = deque('donthateme')

print(dq)
print()

print(dq.__dir__())                 # 메서드 확인
print()

print(dq.pop())                     # 마지막 (오른쪽) 요소 제거
print()

dq = deque('donthateme')
print(dq.popleft())                 # 첫번째 (왼쪽) 요소 제거
print()

dq = deque('donthateme')
print(dq.clear())                   # 전체 제거
print()

dq = deque('donthateme')
dq.append('hit')                    # 오른쪽 추가
print(dq)
print()

dq = deque('donthateme')
dq.appendleft('hit')                # 왼쪽 추가
print(dq)
print()

dq.remove('hit')                    # 해당 아이템 제거
print(dq)
print()

dq.rotate(5)                        # index 0번이 맨 뒤로 n번 회전 (반시계회전)
print(dq)
print()

dq.reverse()                        # 뒤집기
print(dq)
print()