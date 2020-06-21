dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
height, width = list(map(int, input().split()))
roots = [input() for _ in range(height)]
seen = [[False] * width for _ in range(height)]
stacks = []
"""
def dfs(roots, h, w):
  seen[h][w] = True
  for i in range(4):
    next_h = h + dy[i]
    next_w = w + dx[i]
    if next_h < 0 or next_h >= height or next_w < 0 or next_w >= width:
      continue
    if roots[next_h][next_w] == '#' or seen[next_h][next_w]:
      continue
    dfs(roots, next_h, next_w)
"""
sh = 0
sw = 0
gh = 0
gw = 0
for i in range(height):
  for j in range(width):
    if roots[i][j] == 's':
      sh = i
      sw = j
    elif roots[i][j] == 'g':
      gh = i
      gw = j
stacks.append([sh, sw])
seen[sh][sw] = True

while len(stacks) != 0:
  item = stacks.pop()
  sh = item[0]
  sw = item[1]
  for i in range(4):
    nh = sh + dy[i]
    nw = sw + dx[i]
    if nh < 0 or nh >= height or nw < 0 or nw >= width:
      continue
    elif seen[nh][nw] or roots[nh][nw] == '#':
      continue
    else:
      stacks.append([nh, nw])
      seen[nh][nw] = True
if seen[gh][gw]:
  print('Yes')
else:
  print('No')
