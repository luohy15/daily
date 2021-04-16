from typing import List

import sys
sys.path.append("./")
from lib.tree import TreeNode

def invert(root):
    if not root:
        return None
    tmpnode = root.left
    root.left = invert(root.right)
    root.right = invert(tmpnode)
    return root

def tree2arr(root):
    q = []
    nextq = []
    res = []
    if root:
        q.append(root)
    while True:
        ress = []
        while q:
            cur = q.pop(0)
            if cur:
                ress.append(cur.val)
                nextq.append(cur.left)
                nextq.append(cur.right)
            else:
                ress.append(None)
        if ress:
            if not all(v is None for v in ress):
                res.extend(ress)
            q = nextq
            nextq = []
        else:
            break
    return res

class Solution(object):
    """
    暴力
        二叉树转换成数组
        翻转二叉树
        二叉树转换成数组
        比较两个数组
    time: O(n)
    space: O(n)
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        arr1 = tree2arr(root)
        invert(root)
        arr2 = tree2arr(root)
        return arr1 == arr2
