class UnionFind2D:
    def __init__(self, h, w):
        self.h, self.w, self.n = h, w, h*w
        self.parents = [-1] * self.n
    def _find(self, v):
        if self.parents[v] < 0: return v
        self.parents[v] = self._find(self.parents[v])
        return self.parents[v]
    def find(self, y, x):
        assert 0 <= y < self.h and 0 <= x < self.w
        return self._find(y*self.w+x)
    def merge(self, y1, x1, y2, x2):
        assert 0 <= y1 < self.h and 0 <= x1 < self.w
        assert 0 <= y2 < self.h and 0 <= x2 < self.w
        v1, v2 = self._find(y1*self.w+x1), self._find(y2*self.w+x2)
        if v1 == v2: return
        if self._size(v1) < self._size(v2): v1, v2 = v2, v1
        self.parents[v1] += self.parents[v2]
        self.parents[v2] = v1
    def same(self, y1, x1, y2, x2):
        assert 0 <= y1 < self.h and 0 <= x1 < self.w
        assert 0 <= y2 < self.h and 0 <= x2 < self.w
        return self._find(y1*self.w+x1) == self._find(y2*self.w+x2)
    def _size(self, v):
        return -self.parents[self._find(v)]
    def size(self, y, x):
        assert 0 <= y < self.h and 0 <= x < self.w
        return self._size(y*self.w+x)
    def roots(self):
        return [v for v, s in enumerate(self.parents) if s < 0]
    def group(self, y, x):
        assert 0 <= y < self.h and 0 <= x < self.w
        root = self._find(y*self.w+x)
        return [(v//self.w, v%self.w) for v in range(self.n) if self._find(v) == root]
    def groups(self):
        res = [set() for _ in range(self.n)]
        for i in range(self.n):
            res[self._find(i)].add((i//self.w, i%self.w))
        res = [g for g in res if len(g) > 0]
        return res
    def board(self):
        b = [[0] * self.w for _ in range(self.h)]
        cnt = 1
        for g in self.groups():
            if len(g) == 1: continue
            for y, x in g:
                b[y][x] = cnt
            cnt += 1
        return b
    def __str__(self):
        return "\n".join(map(str, self.board()))