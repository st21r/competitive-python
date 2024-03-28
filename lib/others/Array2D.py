class Array2d:
    def __init__(self, h, w, init_val = 0):
        self.h, self.w = h, w
        self.data = [init_val] * (h*w)
    def __call__(self, data):
        assert len(data) == self.h
        for i in range(self.h):
            assert len(data[i]) == self.w
            for j in range(self.w):
                self.data[i*self.w+j] = data[i][j]
    def get(self, i, j):
        if i < 0 or j < 0 or i >= self.h or j >= self.w: return None
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
    def tostr(self, sep=" "):
        res = ""
        for i in range(self.h):
            res += sep.join(map(str, self.data[i*self.w:(i+1)*self.w])) + "\n"
        return res
    def __str__(self):
        return self.tostr()
    def rotate(self):
        assert self.h == self.w
        tmp = [None] * (self.h*self.w)
        for i in range(self.h):
            for j in range(self.w):
                tmp[(self.w-j-1)*self.w+i] = self.get(i, j)
        self.data = tmp
