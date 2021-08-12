def bellman_ford(edges, n, s):
    d = [INF] * n
    d[s] = 0
    for i in range(n):
        for f, t, c in edges:
            if d[f] == INF: continue
            if d[t] > d[f] + c:
                if i == n-1: d[t] = -INF
                else: d[t] = d[f] + c
    for i in range(n):
        for f, t, c in edges:
            if d[f] == INF: continue
            d[t] = min(d[t], d[f] + c)
    return d
