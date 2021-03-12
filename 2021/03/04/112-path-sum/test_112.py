import pytest

import sys
sys.path.append("./")
from lib.tree import buildTree
from main_112 import Solution

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