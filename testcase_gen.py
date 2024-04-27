import sys
import random

def generate():
    h, w = 1000, 1000
    print(h, w)
    for i in range(h):
        for j in range(w):
            print(random.choice(['.', '#']), end='')
        print()
    

with open('input.txt', mode='w') as f:
    sys.stdout = f
    generate()
