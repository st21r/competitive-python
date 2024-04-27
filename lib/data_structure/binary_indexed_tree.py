class BIT:
    def __init__(self, val):
        if type(val) == int:
            self.n = val
            self.data = [0] * (self.n+1)
        elif type(val) == list:
            self.n = len(val)
            self.data = [0] * (self.n+1)
            self.build(val)
        else: raise TypeError(type(val))
    
    def build(self, data):
        for i in range(1, self.n+1):
            self.data[i] += data[i-1]
            j = i + (i & -i)
            if j <= self.n:
                self.data[j] += self.data[i]
    
    class _Element:
        def __init__(self, outer, i, val):
            self.outer = outer
            self.i = i
            self.val = val
        def __iadd__(self, x):
            self.outer.add(self.i, x)
        def __isub__(self, x):
            self.outer.add(self.i, -x)
        def __str__(self):
            return str(self.val)

    def __getitem__(self, i):
        if not (0 <= i < self.n): raise IndexError(i)
        return self._Element(self, i, self.sum(i, i+1))
    
    def __setitem__(self, i, x):
        if not (0 <= i < self.n): raise IndexError(i)
        if x == None: return
        self.add(i, -self.sum(i, i+1))
        self.add(i, x)
    
    def items(self):
        res, tmp = [0] * self.n, 0
        for i in range(self.n):
            s = self._sum(i+1)
            res[i] = s-tmp
            tmp = s
        return res
     
    def __str__(self):
        return "[" + ", ".join(map(str, self.items())) + "]"
    
    def _sum(self, i):
        assert 0 <= i <= self.n
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res
    
    def sum(self, i, j=None):
        if j is None: return self._sum(i)
        return self._sum(j) - self._sum(i)
    
    def add(self, i, x):
        assert 0 <= i < self.n
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def lower_bound(self, x):
        cur, s, k = 0, 0, 1 << (self.n.bit_length()-1)
        while k:
            nxt = cur + k 
            if nxt <= self.n and s + self.data[nxt] < x:
                s += self.data[nxt]
                cur = nxt
            k >>= 1
        return cur
