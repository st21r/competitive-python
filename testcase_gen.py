import sys
import random

n = 200000

def generate():
    print(n)
    

with open('input.txt', mode='w') as f:
    sys.stdout = f
    generate()
