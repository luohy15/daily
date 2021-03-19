from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    迭代
    time: O(n)
    space: O(n)
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res