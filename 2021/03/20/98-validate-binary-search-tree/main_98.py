from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

def check(node, mi, ma):
    if mi != None and node.val <= mi:
        return False
    if ma != None and node.val >= ma:
        return False
    res = True
    if node.left:
        res = res and check(node.left, mi, node.val)
    if node.right:
        res = res and check(node.right, node.val, ma)
    return res

class Solution(object):
    """
    递归
        验证节点是否在范围中(mi,ma)
    time: O(n)
    space: O(n)
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return check(root, None, None)