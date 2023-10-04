box = [list(map(int, input().split())) for _ in range(10)]
start = [1, 1]
dy = [0, 1]
dx = [1, 0]

def find(location):
  y, x = location
  box[y][x] = 9
  for i in range(len(dy)):
    point = box[y+dy[i]][x+dx[i]]
    if point == 0:
      y += dy[i]
      x += dx[i]
      find([y, x])
      break
    if point == 1:
      continue
    if point == 2:
      y += dy[i]
      x += dx[i]
      box[y][x] = 9
      break

    
find(start)

for item in box:
  print(*item)