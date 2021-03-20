from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    递归
        分别递归翻转左右子树
    time: O(n)
    space: O(n)
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmpnode = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(tmpnode)
        return root