from typing import List

class Solution(object):
    """
    递推
    dp[i] = dp[j] and s[j:i] in wordDict
    time: O(n ** 2)
    space: O(n)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordSet = {word for word in wordDict}
        for i in range(1,len(s)+1):
            for j in range(i):
                dp[i] = dp[i] or (dp[j] and s[j:i] in wordSet)
        return dp[len(s)]