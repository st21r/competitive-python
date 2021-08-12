def factorize(x, lim=10**6+10):
    res = []
    for i in range(2, int(lim**0.5)+1):
        cnt = 0
        while not x % i:
            x //= i
            cnt += 1
        if cnt: res.append((i, cnt))
    if x > 1: res.append((x, 1))
    return res
