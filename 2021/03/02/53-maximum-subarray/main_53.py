class Solution(object):
    """
    brute force:
        maintain sum, max
        if sum > max, update max
        if sum < 0, drop sum
    time: O(n)
    space: O(1)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = -10 ** 6
        for n in nums:
            sum += n
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max