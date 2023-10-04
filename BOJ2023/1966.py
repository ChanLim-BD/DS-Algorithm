from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    nums = deque(list(map(int, input().split())))
    idx = deque(list(range(N)))
    cnt = 0

    while nums:
        if nums[0] == max(nums):
            cnt += 1
            nums.popleft()
            pop_idx = idx.popleft()
            if pop_idx == M:
                print(cnt)
        else:
            nums.append(nums.popleft())
            idx.append(idx.popleft())
