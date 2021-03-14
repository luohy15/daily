import collections

class LRUCache(collections.OrderedDict):

    # 初始化lru数据结构
    def __init__(self, capacity: int):
        # 有序字典
        super().__init__()
        # key到链表节点的映射
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        # 如果不在，返回-1
        if key not in self:
            return -1
        # 如果在cache中，更新
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            # 如果在cache中，先删掉
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)