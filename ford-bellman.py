# Вариант с матрицей смежности

n, m = list(map(int, input().split()))
W = [list(map(int, input().split())) for _ in range(m)]


INF = float('inf')
dp = [[INF] * n for _ in range(n)]
dp[0][start] = 0 
for k in range(1, n): 
    for i in range(n): 
         dp[k][i] = dp[k - 1][i]
         for j in range(n):
            dp[k][i] = min(dp[k][i], dp[k - 1][j] + W[j][i])
ans = dp[-1]

'''

Задача: найти кратчайшее расстояние от узла start до каждого из узлов на графе

Алгоритм Форда-Беллмана:

1. Создаём пустой двумерный массив размером n*n. Так в dp[k][i] мы будем на k-том шагу знать кратчайшее расстояние от v до i.
2. n-1 раз оптимизируем веса по следующему правилу:
    Для всех возможный i и всех j, соединённых с i: dp[k][i] = min(dp[k][i], dp[k-1][j] + w[j][i])
3. Массив ответов - последняя строка в матрице dp

'''

# Вариант с графом в виде словаря

def _input(): return list(map(int, input().split()))

n, m, start = _input()
w = [_input() for _ in range(m)]
gr = {}
for i in range(n): gr[i] = {}
for [b, a, c] in w:
    gr[a][b] = c
    gr[b][a] = c
dp = [[INF for _ in range(n)] for _ in range(n)]
dp[0][start] = 0
for k in range(1, n):
    for i in range(n):
        dp[k][i] = dp[k-1][i]
        for j, cost in gr[i].items():
            dp[k][i] = min(dp[k][i], dp[k-1][j] + cost)
ans = dp[-1]
print(*ans)