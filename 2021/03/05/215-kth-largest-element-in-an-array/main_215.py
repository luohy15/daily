class Solution(object):
    """
    brute force:
        sort and print nums[k]
    time: O(nlogn)
    space: O(1)
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]