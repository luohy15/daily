import pytest

from main_112 import TreeNode
from main_112 import Solution

def buildTree(arr):
    if len(arr) == 0:
        return None
    tree = []
    for a in arr:
        if a is None:
            tree.append(None)
        else:
            tree.append(TreeNode(a))
    for i in range(int(len(arr) / 2)):
        li = i * 2 + 1
        ri = i * 2 + 2
        if li < len(arr) and tree[li] is not None:
            tree[i].left = tree[li]
        if ri < len(arr) and tree[ri] is not None:
            tree[i].right = tree[ri]
    return tree[0]

def test1():
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = buildTree(arr)
    targetSum = 22
    assert Solution().hasPathSum(root, targetSum) == True

def test2():
    arr = []
    root = buildTree(arr)
    targetSum = 0
    assert Solution().hasPathSum(root, targetSum) == False