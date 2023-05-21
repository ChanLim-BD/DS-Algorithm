def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)
    

def main():
    print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))


if __name__ == '__main__':
    main()