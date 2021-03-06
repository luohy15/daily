class Solution(object):
    """
    brute force: blabla
    time: O(1)
    space: O(1)
    """
    def traverse(self, matrix):
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        curr_dir = 0
        li = len(matrix)
        lj = len(matrix[0])
        visited = [[False]*lj for i in range(li)]
        i = 0
        j = 0
        count = 1
        res = [matrix[0][0]]
        visited[0][0] = True
        while count < li * lj:
            newi = i + dirs[curr_dir][0]
            newj = j + dirs[curr_dir][1]
            # if valid and not visited: forward
            if newi >= 0 and newi < li and newj >= 0 and newj < lj and not visited[newi][newj]:
                i = newi
                j = newj
                res.append(matrix[i][j])
                visited[i][j] = True
                count += 1
            # else change direction
            else:
                curr_dir += 1
                curr_dir %= 4
        return res
    