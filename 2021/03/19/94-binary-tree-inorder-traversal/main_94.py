from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    递归
    time: O(n)
    space: O(n)
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        if not root:
            return ret
        if (root.left):
            ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        if (root.right):
            ret.extend(self.inorderTraversal(root.right))
        return ret
