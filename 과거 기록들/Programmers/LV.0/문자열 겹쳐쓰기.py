"""
이 함수는 다음과 같은 파라미터를 입력으로 받습니다:

my_string: 원본 문자열
overwrite_string: 덮어쓸 문자열
s: 덮어쓸 시작 인덱스
함수는 다음과 같이 동작합니다:

my_string의 0부터 s - 1까지의 부분 문자열을 가져옵니다. 이 부분은 덮어쓰기 이전의 문자열입니다.
overwrite_string을 가져와서 해당 부분을 덮어씁니다.
my_string의 s + len(overwrite_string)부터 끝까지의 부분 문자열을 가져옵니다. 이 부분은 덮어쓰기 이후의 문자열입니다.
위의 세 부분 문자열을 이어붙여 최종 결과를 반환합니다.
예를 들어, my_string = "Hello, world!", overwrite_string = "there", s = 7인 경우를 생각해봅시다. 이 경우 함수는 다음과 같이 동작합니다:

"Hello, "를 가져옵니다.
"there"로 덮어씁니다.
"world!"를 가져옵니다.
이 세 부분을 이어붙여 "Hello, there!"를 반환합니다.
따라서, 위의 예시에서 solution("Hello, world!", "there", 7)은 "Hello, there!"을 반환합니다.
"""

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


def main():
    print(solution("He11oWor1d", "lloWorl", 2))


if __name__ == '__main__':
    main()
