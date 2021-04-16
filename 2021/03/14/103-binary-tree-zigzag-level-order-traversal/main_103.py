from typing import List
import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    bfs with reversed flag
    time: O(n)
    space: O(n)
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        q = []
        nextq = []
        res = []
        reversed = False
        if root:
            q.append(root)
        while True:
            ress = []
            while q:
                cur = q.pop(0)
                ress.append(cur.val)
                if cur.left:
                    nextq.append(cur.left)
                if cur.right:
                    nextq.append(cur.right)
            if ress:
                if reversed:
                    ress.reverse()
                reversed = not reversed
                res.append(ress)
                q = nextq
                nextq = []
            else:
                break
        return res
