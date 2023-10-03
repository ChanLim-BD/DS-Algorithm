def solution(rsp):
    table = str.maketrans('025', '502')
    # 0 -> 5, 2 -> 0, 5 -> 2
    ans = rsp.translate(table)
    """
    string.translate(table)
    
    table
    필수. 문자열 대체 방법을 지정한 dictionary (또는, 매핑 테이블)
    """
    return ans


def main():
    print(solution('520'))


if __name__ == '__main__':
    main()
