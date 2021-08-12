class Cumsum:
    def __init__(self, a):
        self.n = len(a)
        self.s = [0] * (self.n+1)
        for i in range(self.n):
            self.s[i+1] = self.s[i] + a[i]
    def sum(self, l, r):
        return self.s[r]-self.s[l]
    def __getitem__(self, i):
        return self.s[i]
