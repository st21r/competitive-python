class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y: return
        if self.size(x) < self.size(y): x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.parent[self.find(x)]
