import random

def rand65535():
    return random.randint(0, 65535)

class Solution(object):
    """
    给出一个(0, 65536)的随机整数发生器，需要从30万个数中抽出10万个幸运儿
    time: O(1)
    space: O(1)
    """
    def rand30w(self):
        """
        :rtype: int
        """
        target = 300000
        upper = 2 ** 32 // target * target
        val = upper + 1
        while val > upper:
            bit1 = rand65535() # [0,65535]
            bit2 = rand65535() + 1 # [1,65536]
            val = bit1 * 65536 + bit2 # [1,2**32]
        return val % target + 1
