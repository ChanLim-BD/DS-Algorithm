# def solution(strings, n):
#     answer = []
#     tmp = []
#     for string in strings:
#         tmp.append(string[n])
        
#     for i in range(len(strings)):
#         if strings[tmp.index(sorted(tmp)[i])] not in answer:
#             answer.append(strings[tmp.index(sorted(tmp)[i])])
#         else:
            
                              
#     return answer

def str_sort(strings, n):
    strings.sort() 
    return sorted(strings, key=lambda x:x[n])


print(str_sort(["abce", "abcd", "cdx"], 2))

"""
["abce", "abcd", "cdx"]
"""