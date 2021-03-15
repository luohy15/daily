from typing import List

class Solution(object):
    """
    dp:
        设dp[i][j]表示以i,j为右下角的正方形的边长最大值
        则dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        如果i和j有一个为0，则dp[i][j] = 1
    time: O(nm)
    space: O(nm)
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        ma = 0
        li = len(matrix)
        lj = len(matrix[0])
        dp = [[0] * lj for _ in range(li)]
        for i in range(li):
            for j in range(lj):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ma = max(ma, dp[i][j])
        return ma * ma
