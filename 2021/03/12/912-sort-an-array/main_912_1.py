from typing import List

def heapshiftdown(nums, i, l):
    # i为当前节点，j为待替换节点，初始为左节点
    j = i * 2 + 1
    while j < l:
        # 如果右节点比左节点大，将待替换节点设置为右节点
        if j + 1 < l and nums[j] < nums[j + 1]:
            j = j + 1
        # 大顶堆：如果顶比节点小，则需要替换
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i = j
            j = j * 2 + 1
        else:
            break

def buildheap(nums):
    for i in range(len(nums) // 2 - 1, -1, -1):
        heapshiftdown(nums, i, len(nums))

def heapsort(nums):
    buildheap(nums)
    l = len(nums) - 1
    for i in range(l):
        # 把最大的数放到数组末尾
        nums[0], nums[l - i] = nums[l - i], nums[0]
        # 堆调整范围缩小
        heapshiftdown(nums, 0, l - i)

class Solution(object):
    """
    堆排序：
        建立大顶堆，将堆顶和堆尾交换，然后将堆范围缩小1并调整堆顶，直至堆范围为1
        注意：如果下标从0开始，则左节点为i*2+1，如果下标从1开始，左节点则是i*2
    time: O(nlogn)
    space: O(1)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        heapsort(nums)
        return nums
