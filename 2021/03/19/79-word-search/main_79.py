from typing import List

def dfs(i, j, board, word):
    if len(word) == 1:
        return True
    board[i][j] = ''
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        newi = i + d[0]
        newj = j + d[1]
        if 0 <= newi and newi < len(board) and 0 <= newj and newj < len(board[0]) and board[newi][newj] == word[1]:
            if dfs(newi, newj, board, word[1:]):
                return True
    board[i][j] = word[0]
    return False

class Solution(object):
    """
    DFS
    time: O(m * n * (3 ** l))
    space: O(m * n)
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if dfs(i, j, board, word):
                        return True
        return False