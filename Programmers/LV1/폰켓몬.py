def solution(nums):                     # 3, 1, 2, 3    : 4
    unique_types = len(set(nums))       # 3, 1, 2       : 3

    if len(nums) // 2 > unique_types:   # 2 > 3
        return unique_types
    else:
        return len(nums) // 2           # 2

print(solution([3,1,2,3]))

# def solution(nums):
#     # if len(list(set(nums))) < len(nums)/2:
#     #     return len(list(set(nums)))
#     # return len(nums)/2
    
#     n_dict = {}                   # Hash
    
#     for n in nums:
#         n_dict[n] = 1                 # 같은 종류의 폰켓몬의 중복이 제거된다.
    
#     print(n_dict)
        
#     if len(nums) // 2 <= len(n_dict): # 전체 종류의 수/2와 중복 제거된 종류의 수를 비교
#         return len(nums) // 2         # 전체 종류의 수/2값이 작거나 같다면 즉시 반환
    
#     return len(n_dict)                # 그렇기 않다면 중복 제거된 종류의 수를 반환