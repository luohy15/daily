from typing import List

def mergesort(nums, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    mergesort(nums, l, mid)
    mergesort(nums, mid + 1, r)
    res = []
    i = l
    j = mid + 1
    while i <= mid or j <= r:
        # 如果j已经合并完或者nums[i]小于nums[j]
        if j > r or (i <= mid and nums[i] < nums[j]):
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    nums[l:r+1] = res
    
class Solution(object):
    """
    归并排序：
        将区间切分分别排序，然后合并两个有序数组
        注意要使用闭区间
    time: O(nlogn)
    space: O(n)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        mergesort(nums, 0, len(nums) - 1)
        return nums