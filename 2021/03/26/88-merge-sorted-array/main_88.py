from typing import List

class Solution(object):
    """
    从后往前合并
        不会覆盖掉数组元素
    time: O(n)
    space: O(1)
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] <= nums2[p2]:
                nums1[tail] = nums2[p2]
                p2 -= 1
            else:
                nums1[tail] = nums1[p1]
                p1 -= 1
            tail -= 1
            