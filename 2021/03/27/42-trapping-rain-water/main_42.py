from typing import List

class Solution(object):
    """
    维护单调非增的柱子的下标
    time: O(n)
    space: O(n)
    """
    def trap(self, height: List[int]) -> int:
        # 单调非增柱子的下标
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                # 弹出小于height[i]的柱子
                prev = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                volume = min(height[i], height[stack[-1]]) - height[prev]
                res += distance * volume
            stack.append(i)
        return res
