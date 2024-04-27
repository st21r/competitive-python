class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0: return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def merge(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.size(x) < self.size(y): x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def size(self, x):
        return -self.parents[self.find(x)]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    def groups(self):
        res = [set() for _ in range(self.n)]
        for i in range(self.n):
            res[self.find(i)].add(i)
        res = [x for x in res if len(x) > 0]
        return res
    def __str__(self):
        return '\n'.join([str(x) for x in self.groups()])
