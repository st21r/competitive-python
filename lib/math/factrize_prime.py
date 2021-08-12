def init_factorize(lim=10**6+10, primes=None):
    if primes is None:
        table = [True] * (lim+1)
        table[0:2] = False, False
        for i in range(2, int(lim**0.5)+1):
            if not table[i]: continue
            for j in range(i*2, lim+1, i):
                table[j] = False
        primes = [i for i in range(lim+1) if table[i]]

    def factorize(x):
        res = []
        for p in primes:
            if p ** 2 > x: break
            cnt = 0
            while not x % p:
                x //= p
                cnt += 1
            if cnt: res.append((p, cnt))
        if x > 1: res.append((x, 1))
        return res
    
    return factorize
