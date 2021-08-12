def get_prime(lim):
    table = [True] * (lim+1)
    table[0:2] = False, False
    for i in range(2, int(lim**0.5)+1):
        if not table[i]: continue
        for j in range(i*2, lim+1, i):
            table[j] = False
    return [i for i in range(lim+1) if table[i]]
