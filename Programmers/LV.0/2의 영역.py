def solution(arr):
    ans = []
    tmp = 0
    chk = False
    if arr.count(2) == 0:
        return [-1]
    elif arr.count(2) == 1:
        return [2]
    elif arr.count(2) == 2:
        for i in arr:
            if i == 2 and chk == False:
                ans.append(i)
                chk = True
            elif i != 2 and chk == True:
                ans.append(i)
            elif i == 2 and chk == True:
                ans.append(i)
                break
            else:
                continue
    elif arr.count(2) > 2:
        for i in range(len(arr) -1, -1, -1):
            if arr[i] == 2:
                tmp = i
                break
        for i in range(arr.index(2), tmp + 1):
            ans.append(arr[i])
    return ans


# ---

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]