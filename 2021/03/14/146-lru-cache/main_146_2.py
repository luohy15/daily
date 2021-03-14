class DListNode():
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache():

    # 初始化lru数据结构
    def __init__(self, capacity: int):
        # 空链表
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # key到链表节点的映射
        self.idx = {}
        self.capacity = capacity
        self.len = 0
    
    def get(self, key: int) -> int:
        # 如果不在，返回-1
        if key not in self.idx:
            return -1
        # 如果在cache中，更新
        node = self.idx[key]
        self.remove(node)
        self.append(node)
        return self.idx[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.idx:
            # 如果在cache中，更新值，删掉该节点，添加到末尾
            node = self.idx[key]
            node.val = value
            self.remove(node)
            self.append(node)
        else:
            # 如果不在cache中，添加末尾，如果超出则删除头节点
            node = DListNode(key, value)
            self.idx[key] = node
            self.append(node)
            self.len += 1
            if self.len > self.capacity:
                node = self.head.next
                self.remove(node)
                del self.idx[node.key]
                self.len -= 1
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def append(self, node):
        node.prev = self.tail.prev
        node.prev.next = node
        self.tail.prev = node
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)