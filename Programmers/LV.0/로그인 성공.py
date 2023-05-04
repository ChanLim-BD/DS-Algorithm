def solution(id_pw, db):
    answer = []
    for data in db:
        if data[0] == id_pw[0]:
            if data[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
        else:
            answer.append("fail")
    return answer[0]


def main():
    print(solution(["meosseugi", "1234"], [["rardss", "123"],
          ["yyoom", "1234"], ["meosseugi", "1234"]]))


if __name__ == '__main__':
    main()
