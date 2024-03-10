"""
Longest Increasing Subsequence
가장 긴 증가하는 부분수열

      10  20  10  30  20  50
DP    1   2   1   3   2   4

: 4
"""

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N): # 0 1 2 3 4 5 
    for j in range(i): # i-1 내 기준 왼쪽에 있는 숫자까지 
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) 



"""
가장 긴, 두 수열에 공통적으로 포함되는 경우를 찾아라

        A      C       A       Y       K       P
        C      A       P       C       A       K

첫번째 수열에서 만들 수 있는 모든 부분수열을 꺼낸다.
[A]
[A,C]
[A,A]
[A,Y]
[A,P...]

그런데!, Well_known!
좋은 아이디어, 획기적인 아이디어        

---

M = SALTY   A
N = SALE    A

if 끝의 문자가 같다면, 하나를 하나씩 떼서 없애주고, +1을 해준다.
LCS(M, N) = LCS(M[:-1], N[:-1])

"SALA"              "SAL" + 1

else 같지 않다면,
"""

M = list(str(input()))
N = list(str(input()))

dp = [[0 for _ in range(len(N))] for _ in range(len(M) + 1)]

for i in range(1, len(M) + 1):
    for j in range(1, len(N) + 1):
        if M[i - 1] == N[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[len(M)][len(N)])
