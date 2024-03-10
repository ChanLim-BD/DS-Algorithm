def solution(clothes):
    closet = {}
    result = 1
    
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]
            
     # ex) output: {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
     # 위와 같이 딕셔너리가 만들어진다.
    
    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))