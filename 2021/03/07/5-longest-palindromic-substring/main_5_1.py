# WIP
class Solution(object):
    """
    middle out:
        treat 0, 0.5, 1, ... as the middle of palindrome
        spread to both sides
        find the longest
    time: O(n**2)
    space: O(n)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s