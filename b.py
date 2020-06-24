n, q = list(map(int, input().split()))
parents = [i for i in range(n)]
rank = [1 for i in range(n)]

def root(x):
  if parents[x] != x:
    parents[x] = root(parents[x])
  return parents[x]

def unite(x, y):
  x = root(x)
  y = root(y)
  if x != y:
    if rank[x] > rank[y]:
      parents[y] = x
    else:
      parents[x] = y
      if rank[x] == rank[y]:
        rank[y] += 1
  
for _ in range(q):
  p, a, b = list(map(int, input().split()))
  if p == 0:
    unite(root(a), root(b))
  elif p == 1:
    if root(a) == root(b):
      print('Yes')
    else:
      print('No')
