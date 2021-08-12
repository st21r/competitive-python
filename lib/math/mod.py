MOD_L = 10**6+10
fact = [1, 1] + [0] * (MOD_L-1)
fact_inv = [1, 1] + [0] * (MOD_L-1)
inv = [0, 1] + [0] * (MOD_L-1)
for i in range(2, MOD_L+1):
    fact[i] = fact[i-1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD//i) % MOD
    fact_inv[i] = fact_inv[i-1] * inv[i] % MOD
def mod_comb(n, m):
    if n < m or n < 0 or m < 0: return 0
    return fact[n] * (fact_inv[m] * fact_inv[n-m] % MOD) % MOD
