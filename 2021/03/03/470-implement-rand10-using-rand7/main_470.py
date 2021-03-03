import random

def rand7():
    return random.randint(1, 7)

class Solution(object):
    """
    brute force:
        use 2 bit rand generate [1,49] with equal probability distribution
        choose result in [1,40] then mod 10 plus 1
    time: O(1)
    space: O(1)
    """
    def rand10(self):
        """
        :rtype: int
        """
        val = 41
        while val > 40:
            bit1 = rand7() # [1,7]
            bit2 = rand7() - 1 # [0,6]
            val = bit2 * 7 + bit1 # [1,49]
        return val % 10 + 1