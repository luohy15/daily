class Solution(object):
    """
    brute force: reverse 3 times
    time: O(n)
    space: O(1)
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
