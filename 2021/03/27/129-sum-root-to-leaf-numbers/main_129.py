from typing import List
import sys
sys.path.append("./")
from lib.tree import TreeNode

def dfs(node, s):
    if not node:
        return 0
    s = s * 10 + node.val
    # 如果是叶子节点
    if not node.left and not node.right:
        return s
    # 继续递归
    return dfs(node.left, s) + dfs(node.right, s)

class Solution(object):
    """
    递归
        如果是叶子节点，返回对应的数字
        如果不是叶子节点，继续递归
    time: O(n)
    space: O(n)
    """
    def sumNumbers(self, root: TreeNode) -> int:
        return dfs(root, 0)
