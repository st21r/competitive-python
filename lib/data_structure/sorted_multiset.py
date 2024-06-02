from math import ceil, sqrt
from bisect import bisect_left, bisect_right

class SortedMultiSet():
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a = []):
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                a.append(x)
        n = self.size = len(a)
        num_bucket = int(ceil(sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self):
        for i in self.a:
            for j in i: yield j

    def __reversed__(self):
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other):
        return list(self) == list(other)
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x):
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]: break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x):
        if self.size == 0: return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x
    
    def count(self, x):
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x):
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, b, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]
        return True
    
    def _pop(self, a, b, i):
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans

    def remove(self, x):
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x: return False
        self._pop(a, b, i)
        return True
    
    def __getitem__(self, i):
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def pop(self, i = -1):
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    
    def index(self, x):
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans
    
    def index_right(self, x):
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
