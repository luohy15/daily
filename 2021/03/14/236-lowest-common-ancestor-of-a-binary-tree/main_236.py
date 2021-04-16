import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    递归
        两种找到的情况
        1. 在左右子树中
        2. 左右子树+当前节点
    time: O(n)
    space: O(n)
    """
    def __init__(self):
        self.ans = None

    def check(self, cur, p, q):
        if not cur:
            return False
        f1 = self.check(cur.left, p, q)
        f2 = self.check(cur.right, p, q)
        if f1 and f2 or ((f1 or f2) and (cur.val == p.val or cur.val == q.val)):
            self.ans = cur
        return f1 or f2 or cur.val == p.val or cur.val == q.val

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.check(root, p, q)
        return self.ans
