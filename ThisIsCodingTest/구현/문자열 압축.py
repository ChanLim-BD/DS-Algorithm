def solution(s):
    answer = len(s) # 8

    for step in range(1, len(s) // 2 + 1): # 1 2 3 4
        compressed = ""
        prev = s[0:step] # 0:1 - 1칸, 0:2 - 2칸, 0:3 - 3칸, 0:4 - 4칸
        # a, aa, aab, aabb
        # a, ab, aba, abab, ababc, ababcd, ababcdc, ababcdcd
        count = 1

        for j in range(step, len(s), step): # 1~8 1, 2~8 2, 3~8 3, 4~8 4
            if prev == s[j:j + step]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev  
                else:
                    compressed += prev
                prev = s[j:j + step]
                count = 1
        if count >= 2:    
            compressed += str(count) + prev  
        else: 
            compressed += prev
        answer = min(answer, len(compressed))
    
    return answer

print(solution("aabbaccc")) # 7
print(solution("ababcdcdababcdcd"))# 9
print(solution("abcabcdede")) # 8
print(solution("abcabcabcabcdededededede")) # 14
print(solution("xababcdcdababcdcd"))# 17