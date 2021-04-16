class Solution(object):
    """
    breadth first search
    time: O(m*n)
    space: O(min(m,n))
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
                    # bfs from i,j
                    q = [[i,j]]
                    grid[i][j] = "0"
                    while len(q) > 0:
                        cur = q.pop(0)
                        # four direction bfs
                        for d in [[-1,0], [1,0], [0,-1], [0,1]]:
                            newi = cur[0] + d[0]
                            newj = cur[1] + d[1]
                            # if valid and 1
                            if newi >= 0 and newi < li and newj >= 0 and newj < lj and grid[newi][newj] == "1":
                                q.append([newi, newj])
                                grid[newi][newj] = "0"
        return res
