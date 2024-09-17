def _input(): return list(map(int, input().split()))

n, m, start = _input()
w = [_input() for _ in range(m)]
gr = {}
for i in range(n): gr[i] = {}
for [b, a, c] in w:
    gr[a][b] = c
    # gr[b][a] = c ЕСЛИ ГРАФ НЕ ОРИЕНТИРОВАН
dp = [[INF for _ in range(n)] for _ in range(n)]
dp[0][start] = 0
for k in range(1, n):
    for i in range(n):
        dp[k][i] = dp[k-1][i]
        for j, cost in gr[i].items(): dp[k][i] = min(dp[k][i], dp[k-1][j] + cost)
ans = dp[-1]
print(*ans)
