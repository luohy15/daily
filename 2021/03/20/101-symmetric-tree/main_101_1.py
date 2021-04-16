from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

def check(node1, node2):
    if node1 == None and node2 == None:
        return True
    if node1 == None or node2 == None:
        return False
    return node1.val == node2.val and check(node1.left, node2.right) and check(node1.right, node2.left)

class Solution(object):
    """
    递归
        一个向左，一个向右
    time: O(n)
    space: O(n)
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        return check(root, root)
