class Seg(object):
    def __init__(self, lsum, rsum, isum, msum):
        self.lsum = lsum
        self.rsum = rsum
        self.isum = isum
        self.msum = msum

def pushup(ll, rr):
    lsum = max(ll.lsum, ll.isum + rr.lsum)
    rsum = max(rr.rsum, ll.rsum + rr.isum)
    isum = ll.isum + rr.isum
    msum = max(max(ll.msum, rr.msum), ll.rsum + rr.lsum)
    return Seg(lsum, rsum, isum, msum)

def get(nums, l, r):
    if (l == r):
        val = nums[l]
        return Seg(val, val, val, val)
    else:
        m = int((l + r) / 2)
        return pushup(get(nums, l, m), get(nums, m + 1, r))

class Solution(object):
    """
    maintain four sum similar to segment tree:
        lsum: maximum subarray sum start from left
        rsum: maximum subarray sum end with right
        isum: subarray sum
        msum: maximum subarray sum
    so that:
        res = get(nums, l, r).msum
        get(nums, l, r): pushup(get(nums, l, m), get(nums, m+1, r))
        pushup for four sum
    time: O(n)
    space: O(logn)
    """
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return get(nums, 0, len(nums) - 1).msum
