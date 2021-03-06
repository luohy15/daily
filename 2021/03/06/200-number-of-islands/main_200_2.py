class UF(object):
    def __init__(self, n):
        self.array = [i for i in range(n)]
        self.count = 0

    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa == fb:
            return
        else:
            self.array[fa] = fb
            self.count += 1

    def find(self, a):
        if self.array[a] == a:
            return a
        else:
            return self.find(self.array[a])

class Solution(object):
    """
    union find
    time: O(m*n)
    space: O(m*n)
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        li = len(grid)
        lj = len(grid[0])
        total = 0
        uf = UF(li * lj)
        for i in range(li):
            for j in range(lj):
                if grid[i][j] == "1":
                    total += 1
                    grid[i][j] = "0"
                    for d in [[-1,0], [1,0], [0,-1], [0,1]]:
                        newi = i + d[0]
                        newj = j + d[1]
                        if newi >= 0 and newi < li and newj >= 0 and newj < lj and grid[newi][newj] == "1":
                            uf.union(i * lj + j, newi * lj + newj)
        return total - uf.count
