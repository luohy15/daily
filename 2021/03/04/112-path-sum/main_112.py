class Solution(object):
    """
    brute force:
        recursive: use system stack
    time: O(n)
    space: O(logn)@average O(n)@worst
    """
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not (root.left or root.right):
            return root.val == targetSum
        newTargetSum = targetSum - root.val
        return self.hasPathSum(root.left, newTargetSum) or self.hasPathSum(root.right, newTargetSum)
