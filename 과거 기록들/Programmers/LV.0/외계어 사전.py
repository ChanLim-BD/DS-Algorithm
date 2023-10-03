def solution1(spell, dic):
    spell.sort()
    dic.sort()
    ans = []
    for s in dic:
        x = list(sorted(s))
        for c in spell:
            if c in x:
                ans.append(c)
                if ans == x and ans == spell:
                    return 1
            else:
                ans.clear()
                flag = 2
    return flag


def solution2(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2


def solution(spell: list, dic: list):
    spell = {i: 0 for i in spell}

    for x in dic:
        if len(x) == len(spell):
            for y in x:
                if y in spell:
                    spell[y] += 1
                else:
                    break
            if len(set(spell.values())) == 1 and sum(set(spell.values())) == 1:
                return 1
            spell = {i: 0 for i in spell}

    return 2


def solution3(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2


def main():
    print(solution(["s", "o", "m", "d"], [
          "moos", "dzx", "smm", "sunmmo", "som"]))


if __name__ == '__main__':
    main()
