class LRUCache:

    # 初始化lru数据结构
    def __init__(self, capacity: int):
        # cache链表
        self.cache = []
        # key到链表节点的映射
        self.idx = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.idx:
            # 如果在cache中，更新
            self.cache.remove(self.idx[key])
            self.cache.append(self.idx[key])
            return self.cache[-1][1]
        else:
            # 如果不在，返回-1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.idx:
            # 如果在cache中，先删掉
            self.cache.remove(self.idx[key])
        else:
            # 如果不在cache中，且cache是满的，需要腾出位置
            if len(self.cache) == self.capacity:
                del self.idx[self.cache.pop(0)[0]]
        # 添加到尾部
        self.idx[key] = (key, value)
        self.cache.append(self.idx[key])



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
