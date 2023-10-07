def solution(participant, completion):
    hashdic = {}
    sumHash = 0
    for par in participant:
        hashdic[hash(par)] = par
        sumHash += hash(par)
    print(hashdic)
    print(sumHash)
    for comp in completion:
        sumHash -= hash(comp)
    return hashdic[sumHash]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], 
               ["josipa", "filipa", "marina", "nikola"]))