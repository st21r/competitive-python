def get_divisor(num):
    f_divs, l_divs = [], []
    for i in range(1, int(num**0.5)+1):
        if not num % i:
            f_divs.append(i)
            if i != num // i:
                l_divs.append(num // i)
    return f_divs + l_divs[::-1]


if __name__ == "__main__":
    for i in range(100):
        print(i, get_divisor(i))
