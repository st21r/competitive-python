import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque
from itertools import product
INF = int(1e18); arr4 = ((-1, 0), (0, -1), (1, 0), (0, 1))
def dmp(*args, sep=" ", end="\n"): print(*args, sep=sep, end=end, file=sys.stderr)
if "DEBUG" not in sys.argv: dmp = lambda *args: None
