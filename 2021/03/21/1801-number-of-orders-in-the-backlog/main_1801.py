from typing import List
import heapq

class Solution(object):
    """
    积压订单
        使用堆（Python heapq）维护buy和sell队列
        其中buy堆基于-price排序（大顶堆）
        如果buy，sell均不为空，且buy堆顶价格大于sell堆顶价格，则发生交易
    time: O(nlogn)
    space: O(n)
    """
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy, sell = [], []
        res = 0
        mod = 10 ** 9 + 7
        for o in orders:
            price, amount, otype = o[0], o[1], o[2]
            res += amount
            if otype == 0:
                heapq.heappush(buy, (-price, amount))
            else:
                heapq.heappush(sell, (price, amount))
            while buy and sell and -buy[0][0] >= sell[0][0]:
                bi = heapq.heappop(buy)
                si = heapq.heappop(sell)
                if bi[1] <= si[1]:
                    heapq.heappush(sell, (si[0], si[1] - bi[1]))
                    res -= 2 * bi[1]
                else:
                    heapq.heappush(buy, (bi[0], bi[1] - si[1]))
                    res -= 2 * si[1]
        return res % mod