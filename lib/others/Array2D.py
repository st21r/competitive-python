class Array2d:
    def __init__(self, h, w, init_v = 0, out_v = None):
        self.h, self.w = h, w
        self.data = [init_v] * (h*w)
        self.out_v = out_v
    def __call__(self, data): # build with 2d-list
        assert len(data) == self.h
        for i in range(self.h):
            assert len(data[i]) == self.w
            for j in range(self.w):
                self.data[i*self.w+j] = data[i][j]
    def get(self, i, j):
        if i < 0 or j < 0 or i >= self.h or j >= self.w: return self.out_v
        return self.data[i*self.w+j]
    def set(self, i, j, value):
        if i < 0 or j < 0 or i >= self.h or j >= self.w: return False
        self.data[i*self.w+j] = value
        return True
    def __getitem__(self, idx):
        assert type(idx) == tuple
        i, j = idx
        return self.get(i, j)
    def __setitem__(self, idx, value):
        assert type(idx) == tuple
        i, j = idx
        self.set(i, j, value)
    def dmp(self, sep=" "):
        res = ""
        for i in range(self.h):
            res += sep.join(map(str, self.data[i*self.w:(i+1)*self.w])) + "\n"
        return res
    def __str__(self):
        return self.dmp()
    def all(self, y1, x1, y2, x2, val):
        assert y1 <= y2
        assert x1 <= x2
        if y1 < 0 or y2 > self.h: return False
        if x1 < 0 or x2 > self.w: return False
        for y in range(y1, y2):
            for x in range(x1, x2):
                if self.data[y*self.w+x] != val:
                    return False
        return True
    def fill(self, y1, x1, y2, x2, val):
        assert y1 <= y2
        assert x1 <= x2
        if y1 < 0 or y2 > self.h: return False
        if x1 < 0 or x2 > self.w: return False
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.data[y*self.w+x] = val
    def rotate(self):
        assert self.h == self.w
        tmp = [None] * (self.h*self.w)
        for i in range(self.h):
            for j in range(self.w):
                tmp[(self.w-j-1)*self.w+i] = self.get(i, j)
        self.data = tmp
