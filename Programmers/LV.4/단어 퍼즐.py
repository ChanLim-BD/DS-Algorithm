import sys

def solution(strs, t):
    strs = set(strs) # 중복제거 
    dp = [sys.maxsize]*(len(t)+1)
    dp[0] = 0 # dp의 첫번째 값은 아무 의미없기 때문에 0으로 처리
    
    for i in range(len(t)):
        for j in range(1, 6): # 제한 사항에 모든 단어 조각의 길이는 1 이상 5 이하
            e = i + j
            if e > len(t):
                break
        
            string = t[i:e]
            if string in strs:
                dp[e] = min(dp[i]+1, dp[e])
                
    return -1 if dp[-1] == sys.maxsize else dp[-1]


print(solution(["ba","na","n","a"], "banana"))
print(solution(["app","ap","p","l","e","ple","pp"], "apple"))
print(solution(["ba","an","nan","ban","n"], "banana"))