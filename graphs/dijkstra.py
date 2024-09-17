def _input(): return list(map(int, input().split()))
INF = float('inf')

n, m = _input()
w = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n): w[i][i] = 0
for _ in range(m):
  a, b, cost = _input()
  w[a][b] = cost
  # w[b][a] = cost ЕСЛИ ГРАФ НЕ ОРИЕНТИРОВАННЫЙ


dist = [INF for _ in range(n)]
dist[start] = 0
used = [0 for _ in range(n)]
min_dist = 0
min_vertex = start
while min_dist < INF:
  i = min_vertex 
  used[i] = True 
  for j in range(n): dist[j] = min(dist[j], dist[i] + w[i][j])
  min_dist = INF
  for j in range(n):
      if not used[j] and dist[j] < min_dist: min_dist, min_vertex = dist[j], j
