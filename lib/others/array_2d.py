class Array2d:
    def __init__(self, h, w, mode = int, init_val = 0, out_val = None):
        self.h, self.w = h, w
        self.data = [init_val] * (h*w)
        self.init_val = init_val
        self.out_val = out_val
        assert mode in [int, str]
        self.mode = mode
    def __call__(self, data): # build with 2d-list
        assert len(data) == self.h
        for i in range(self.h):
            assert len(data[i]) == self.w
            for j in range(self.w):
                self.data[i*self.w+j] = data[i][j]
    def input(self):
        for i in range(self.h):
            l = input() if self.mode == str else list(map(int, input().split()))
            assert len(l) == self.w
            for j in range(self.w):
                self.data[i*self.w+j] = l[j]
        return self
    def _get(self, i, j):
        if i < 0 or j < 0 or i >= self.h or j >= self.w: return self.out_val
        return self.data[i*self.w+j]
    def _set(self, i, j, value):
        if i < 0 or j < 0 or i >= self.h or j >= self.w: return False
        self.data[i*self.w+j] = value
        return True
    def __getitem__(self, idx):
        assert type(idx) == tuple
        i, j = idx
        return self._get(i, j)
    def __setitem__(self, idx, value):
        assert type(idx) == tuple
        i, j = idx
        self._set(i, j, value)
    def row(self, i):
        assert 0 <= i < self.h
        return self.data[self.w*i:self.w*(i+1)]
    def col(self, i):
        assert 0 <= i < self.w
        return self.data[i::self.w]
    def get_copy(self):
        a = Array2d(self.h, self.w, mode=self.mode, init_val=self.init_val, out_val=self.out_val)
        a.data = self.data[:]
        return a
    def __str__(self):
        res = ""
        sep = "" if self.mode == str else " "
        for i in range(self.h):
            res += sep.join(map(str, self.data[i*self.w:(i+1)*self.w])) + "\n"
        return res
    def all(self, val, y1=0, x1=0, y2=None, x2=None):
        if y2 is None: y2 = self.h
        if x2 is None: x2 = self.w
        assert y1 <= y2 and x1 <= x2
        y1, y2 = max(y1, 0), min(y2, self.h)
        x1, x2 = max(x1, 0), min(x2, self.w)
        for y in range(y1, y2):
            for x in range(x1, x2):
                if self.data[y*self.w+x] != val:
                    return False
        return True
    def any(self, val, y1=0, x1=0, y2=None, x2=None):
        if y2 is None: y2 = self.h
        if x2 is None: x2 = self.w
        assert y1 <= y2 and x1 <= x2
        y1, y2 = max(y1, 0), min(y2, self.h)
        x1, x2 = max(x1, 0), min(x2, self.w)
        for y in range(y1, y2):
            for x in range(x1, x2):
                if self.data[y*self.w+x] == val:
                    return True
        return False
    def count(self, val, y1=0, x1=0, y2=None, x2=None):
        if y2 is None: y2 = self.h
        if x2 is None: x2 = self.w
        assert y1 <= y2 and x1 <= x2
        y1, y2 = max(y1, 0), min(y2, self.h)
        x1, x2 = max(x1, 0), min(x2, self.w)
        cnt = 0
        for y in range(y1, y2):
            for x in range(x1, x2):
                cnt += self.data[y*self.w+x] == val
        return cnt 
    def fill(self, val, y1=0, x1=0, y2=None, x2=None):
        if y2 is None: y2 = self.h
        if x2 is None: x2 = self.w
        assert y1 <= y2 and x1 <= x2
        y1, y2 = max(y1, 0), min(y2, self.h)
        x1, x2 = max(x1, 0), min(x2, self.w)
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.data[y*self.w+x] = val
    def rotate(self):
        tmp = [None] * (self.h*self.w)
        h, w = self.w, self.h
        for i in range(h):
            for j in range(w):
                tmp[i*w+j] = self._get(w-j-1, i)
        self.data = tmp
        self.h, self.w = h, w
