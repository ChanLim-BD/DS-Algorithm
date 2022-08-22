# from quickSortCount import *
from mergeSortCount import *

def do_sort(input_file):

    data_file = open(input_file)
    A = []
    for line in data_file.readlines():
        lpn = line.split()[0]
        A.append(lpn)

    count = {} # 딕셔너리
    for i in A:
        try: count[i] += 1
        except: count[i] = 1
    # sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    # print(sort_count[0])

    tmp = list(count.items())

    # quickSort(tmp, 0, len(tmp)-1)
    mergeSort(tmp, 0, len(tmp)-1)

    for i in range(len(tmp) - 1, len(tmp) - 11, -1):
         print(tmp[i][0], end=" ")
         print(tmp[i][1])
    print("")

if __name__ == "__main__":
    do_sort('ch9\linkbench_short.trc')