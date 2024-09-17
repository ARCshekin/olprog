def _input(): return list(map(int, input().split()))


n, m = _input()
w = [_input() for _ in range(m)]
w.sort(key = lambda x: x[2])
joined = [0 for _ in range(n)]
joined[w[0][0]] = 1
joined[w[0][1]] = 1
ans = w[0][2]
cnt = 2
i = 1
checked = [0 for _ in range(m)]
checked[0] = 1
while cnt != n and i != m:
    a, b, c = w[i]
    if joined[a] and (not joined[b]):
        joined[b] = 1
        ans += c
        cnt += 1
        checked[i] = 1
        i = 1
    elif joined[b] and (not joined[a]):
        joined[a] = 1
        ans += c
        cnt += 1
        checked[i] = 1
        i = 1
    else:
        i += 1
if cnt == n: print(ans)
else: print('Not enough connections')
