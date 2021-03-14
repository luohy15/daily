# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
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