class Solution(object):
    """
    dynamic programming:
        isPalindrome[i][j] = isPalindrome[i+1][j-1] && s[i] == s[j]
    time: O(n**2)
    space: O(n**2)
    """
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        isPalindrome = [[False]*l for _ in range(l)]
        maxl = 0
        res = ""
        for length in range(l):
            for i in range(l):
                j = i + length
                if j >= l:
                    break
                if length == 0:
                    isPalindrome[i][j] = True
                elif length == 1:
                    isPalindrome[i][j] = s[i] == s[j]
                else:
                    isPalindrome[i][j] = s[i] == s[j] and isPalindrome[i + 1][j - 1]
                if isPalindrome[i][j] and length >= maxl:
                    maxl = length
                    res = s[i:j+1]
        return res