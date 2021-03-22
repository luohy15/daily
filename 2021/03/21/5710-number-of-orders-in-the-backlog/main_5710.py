from typing import List

class Solution(object):
    """
    积压订单
        用map维护buy和sell的积压
        模拟判断
    time: O(1)
    space: O(1)
    """
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = {}
        sell = {}
        mod = 10 ** 9 + 7
        for order in orders:
            if order[2] == 0:
                # buy
                if order[0] in buy:
                    buy[order[0]] += order[1]
                else:
                    buy[order[0]] = order[1]
            else:
                # sell
                if order[0] in sell:
                    sell[order[0]] += order[1]
                else:
                    sell[order[0]] = order[1]
            bma = 0
            smi = mod
            if buy:
                bma = max(buy, key=int)
            if sell:
                smi = min(sell, key=int)
            # have a transaction
            while bma >= smi:
                # transaction amount
                ta = min(buy[bma], sell[smi])
                buy[bma] -= ta
                sell[smi] -= ta
                if buy[bma] == 0:
                    del buy[bma]
                if sell[smi] == 0:
                    del sell[smi]
                bma = 0
                smi = mod
                if buy:
                    bma = max(buy, key=int)
                if sell:
                    smi = min(sell, key=int)
        res = 0
        for key in buy.keys():
            res += buy[key]
            res %= mod
        for key in sell.keys():
            res += sell[key]
            res %= mod
        return res