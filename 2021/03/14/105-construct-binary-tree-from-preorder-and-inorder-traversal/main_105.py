from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

class Solution(object):
    """
    前序遍历的第一个元素是root，在中序遍历中找到root划分左右子树，递归build
    time: O(n)
    space: O(n)
    """
    def arr2tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) <= 0:
            return
        val = preorder[0]
        node = TreeNode(val)
        idx = inorder.index(val)
        node.left = self.arr2tree(preorder[1:idx+1], inorder[:idx])
        node.right = self.arr2tree(preorder[idx+1:], inorder[idx+1:])
        return node