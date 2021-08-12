class SegmentTree:
    def __init__(self, n, func=lambda x, y: min(x, y), ide=float("inf")):
        self.n, self.m = n, 1 << (n-1).bit_length()
        self.data = [ide] * (self.m*2)
        self.func, self.ide = func, ide

    def build(self, data):
        for i, x in enumerate(data):
            self.data[self.m+i] = x
        for i in range(self.m-1, 0, -1):
            self.data[i] = self.func(self.data[i*2], self.data[i*2+1])

    def update(self, i, x):
        i += self.m
        self.data[i] = x
        while i > 1:
            i >>= 1
            self.data[i] = self.func(self.data[i*2], self.data[i*2+1])

    def query(self, l, r):
        l += self.m; r += self.m 
        res = self.ide
        while l < r:
            if l & 1:
                res = self.func(res, self.data[l])
                l += 1
            if r & 1:
                res = self.func(res, self.data[r-1])
            l >>= 1; r >>= 1
        return res
  
    def get(self, i):
        return self.data[self.m+i]
    
    def get_data(self):
        return self.data[self.m:self.m+self.n]

    def __setitem__(self, idx, val):
        assert isinstance(idx, int) and -self.n <= idx < self.n
        self.update(idx % self.n, val)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            l, r, _ = idx.indices(self.n)
            assert l <= r
            return self.query(l, r)
        if isinstance(idx, int) and -self.n <= idx < self.n:
            return self.get(idx % self.n)
        raise AssertionError
