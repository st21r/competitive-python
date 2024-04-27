class Double_BIT:
    class _BIT:
        def __init__(self, n):
            self.n = n
            self.data = [0] * (self.n+1)
        def sum(self, i):
            res = 0
            while i > 0:
                res += self.data[i]
                i -= i & -i
            return res
        def add(self, i, x):
            i += 1
            while i <= self.n:
                self.data[i] += x
                i += i & -i
        
    def __init__(self, n):
        self.n = n
        self.p = self._BIT(n)
        self.q = self._BIT(n)

    def __getitem__(self, i):
        if not (0 <= i < self.n): raise IndexError(i)
        return self.sum(i, i+1)
    
    def add(self, l, r, x):
        assert 0 <= l < r <= self.n
        self.p.add(l, -x*l)
        self.p.add(r, x*r)
        self.q.add(l, x)
        self.q.add(r, -x)
    
    def _sum(self, i):
        assert 0 <= i <= self.n
        return self.p.sum(i) + self.q.sum(i) * i
    
    def sum(self, i, j=None):
        if j is None: return self._sum(i)
        return self._sum(j) - self._sum(i)
