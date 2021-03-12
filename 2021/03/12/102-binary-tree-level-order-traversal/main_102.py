from typing import List
import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    bfs
    time: O(n)
    space: O(n)
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = []
        nextq = []
        res = []
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
                res.append(ress)
                q = nextq
                nextq = []
            else:
                break
        return res