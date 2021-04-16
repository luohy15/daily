import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    标记
        1. 标记p到root的路径
        2. 标记q到root的路径，碰到了就返回
    time: O(n)
    space: O(n)
    """
    def __init__(self):
        self.fa = {}
        self.vis = set()

    def dfs(self, curr):
        if curr.left:
            self.fa[curr.left.val] = curr
            self.dfs(curr.left)
        if curr.right:
            self.fa[curr.right.val] = curr
            self.dfs(curr.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root)
        self.fa[root.val] = None
        curr = p
        while curr:
            self.vis.add(curr.val)
            curr = self.fa[curr.val]
        curr = q
        while curr:
            if curr.val in self.vis:
                return curr
            curr = self.fa[curr.val]
        return None
