import sys
import pypyjit
input = lambda: sys.stdin.buffer.readline()
inputstr = lambda: sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**7)
pypyjit.set_param('max_unroll_recursion=0')
