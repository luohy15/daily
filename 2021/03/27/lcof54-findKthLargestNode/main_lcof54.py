from typing import List
import sys
sys.path.append("./")
from lib.tree import TreeNode

def dfs(node, remain):
    if not node:
        return [remain, 0]
    ret = dfs(node.right, remain)
    remain = ret[0]
    if ret[0] == 0:
        return ret
    remain -= 1
    if remain == 0:
        return [0, node.val]
    return dfs(node.left, remain)

class Solution(object):
    """
    反向后序遍历
    time: O(n)
    space: O(n)
    """
    def kthLargest(self, root: TreeNode, k: int) -> int:
        return dfs(root, k)[1]