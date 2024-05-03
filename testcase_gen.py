import sys
import random
import string

def generate():
    n = 5000
    m = 1000
    print(50, end=" ")
    for i in range(n):
        print(random.choice(string.ascii_lowercase), end='')
    print()
    for i in range(m):
        for _ in range(500000//m):
            print(random.choice(string.ascii_lowercase), end='')
        print()
    

with open('input.txt', mode='w') as f:
    sys.stdout = f
    generate()
