def solution(numbers):
    finder = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
    for idx, num in enumerate(finder):
        numbers = numbers.replace(num, str(idx))
    return int(numbers)


def main():
    print(solution("onetwothreefourfivesixseveneightninezero"))


if __name__ == '__main__':
    main()
