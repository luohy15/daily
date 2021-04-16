def dfs(grid, i, j):
    grid[i][j] = "0"
    for d in [[-1,0], [1,0], [0,-1], [0,1]]:
        newi = i + d[0]
        newj = j + d[1]
        if newi >= 0 and newi < len(grid) and newj >= 0 and newj < len(grid[0]) and grid[newi][newj] == "1":
            dfs(grid, newi, newj)

class Solution(object):
    """
    depth first search
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
        res = 0
        for i in range(li):
            for j in range(lj):
                if grid[i][j] == "1":
                    res += 1
                    dfs(grid, i, j)
        return res
