def solution(arr, query):
    for k, q in enumerate(query):
        print(k, q)
        if k % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    return arr

def main():
    print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))


if __name__ == '__main__':
    main()