class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (self.n+1)
    
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
    
    def get_data(self):
        res, tmp = [0] * self.n, 0
        for i in range(self.n):
            s = self._sum(i+1)
            res[i] = s-tmp
            tmp = s
        return res

    def __getitem__(self, i):
        return self.sum(i, i+1)
