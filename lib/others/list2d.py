class list2d:
    def __init__(self, h: int, w: int, init_val: int = 0):
        self.h, self.w = h, w
        self.data = [init_val] * (h*w)
    def __call__(self, data):
        assert len(data) == self.h
        for i in range(self.h):
            assert len(data[i]) == self.w
            for j in range(self.w):
                self.data[i*self.w+j] = data[i][j]
    def __getitem__(self, idx):
        if type(idx) == int: return self.data[idx]
        elif type(idx) == tuple:
            i, j = idx
            assert i < self.h and j < self.w
            return self.data[i*self.w+j]
        assert 0
    def __setitem__(self, idx, value):
        if type(idx) == int: self.data[idx] = value
        elif type(idx) == tuple:
            i, j = idx
            assert i < self.h and j < self.w
            self.data[i*self.w+j] = value
        else: assert 0
    def __str__(self):
        res = ""
        for i in range(self.h):
            res += " ".join(map(str, self.data[i*self.w:(i+1)*self.w])) + "\n"
        return res
