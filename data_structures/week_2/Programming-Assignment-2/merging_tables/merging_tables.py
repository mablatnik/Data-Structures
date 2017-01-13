# python3

import sys

class DisjointSet(object):
    def __init__(self, n, lines):
        self.n = n
        self.lines = [0] + lines
        self.rank = [0] * (n+1)
        self.parent = list(range(0, n + 1))
        self.max = max(self.lines)

    def getParent(self, x):
        parent_update = []

        root = x
        while root != self.parent[root]:
            parent_update.append(self.parent[root])
            root = self.parent[root]

        # path compression
        for i in parent_update:
            self.parent[i] = root

        return root

    def merge(self, destination, source):
        src_root = self.getParent(source)
        dest_root = self.getParent(destination)

        if src_root == dest_root:
            return

        if self.rank[src_root] >= self.rank[dest_root]:
            self.parent[src_root] = dest_root
        else:
            self.parent[dest_root] = src_root
            if self.rank[src_root] == self.rank[dest_root]:
                self.rank[src_root] += 1

        self.lines[dest_root] += self.lines[src_root]
        self.lines[src_root] = 0

        if self.max < self.lines[dest_root]:
            self.max = self.lines[dest_root]

    def get_max(self):
        return self.max

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    lines = list(map(int, sys.stdin.readline().split()))

    disjoint_set = DisjointSet(n, lines)
    for i in range(m):
        destination, source = map(int, sys.stdin.readline().split())
        disjoint_set.merge(destination, source)
        print(disjoint_set.get_max())