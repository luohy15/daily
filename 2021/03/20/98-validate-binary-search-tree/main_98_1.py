from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    中序遍历
        记录前一个节点的值
    time: O(n)
    space: O(n)
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        curr = root
        val = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if val == None or curr.val > val:
                val = curr.val
            else:
                return False
            curr = curr.right
        return True