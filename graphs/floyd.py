def _input(): return list(map(int, input().split()))
inf = float('inf')

n, m = _input()
w = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n): w[i][i] = 0
for _ in range(m):
  a, b, cost = _input()
  w[a][b] = cost
  # w[b][a] = cost ЕСЛИ ГРАФ НЕ ОРИЕНТИРОВАН

for k in range(n): 
    for i in range(n):
        for j in range(n): 
            w[i][j] = min(w[i][j], w[i][k] + w[k][j])
