def is_prime(x):
    if x == 2: return True
    if x == 1 or not x % 2: return False
    for i in range(3, int(x**0.5)+1, 2):
        if not x % i: return False
    else: return True
