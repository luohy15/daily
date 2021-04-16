def partition(nums, left, right):
    """
    return pivot's idx
    """
    pivot = nums[left]
    l = left + 1
    r = right
    while l <= r:
        if nums[l] < pivot and nums[r] > pivot:
            nums[r], nums[l] = nums[l], nums[r]
            l += 1
            r -= 1
        if nums[l] >= pivot:
            l += 1
        if nums[r] <= pivot:
            r -= 1
    nums[left], nums[r] = nums[r], nums[left]
    return r

def quickselect(nums, l, r, k):
    idx = partition(nums, l, r)
    if idx == k:
        return nums[idx]
    else:
        if idx < k:
            return quickselect(nums, idx + 1, r, k)
        else:
            return quickselect(nums, l, idx - 1, k)

class Solution(object):
    """
    quick select:
        use partition
    time: O(n)@expect O(n**2)@worst
    space: O(logn)
    """
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return quickselect(nums, 0, len(nums) - 1, k - 1)
