# 定义一个双向节点
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}  # cache 是一个字典，用来存放所有的key-node对，字典中的value存放的是node
        self.head = DLinkedNode()  # 初始化一个头
        self.tail = DLinkedNode()  # 初始化一个尾
        self.head.next = self.tail  # 建立头尾的双向链接，头-->尾
        self.tail.prev = self.head  # 建立头尾的双向链接，头<--尾

        self.capacity = capacity
        self.size = 0  # 用来判断添加进的node数量是否超过了容量

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            # 如果存在，从字典中获取node，并把该node放在双向链表最前边
            node = self.cache[key]
            self.move_to_head(node)
            return node.value

        else:
            # 如果不存在，返回-1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            # 如果存在，从字典中获取node，更新node值，并将该node放在双向链表最前边
            node = self.cache[key]
            node.value = value  # 更新value值
            self.move_to_head(node)  # 将该node放到最前边
        else:
            # 如果不存在，创建node，放在双向链表最前边，并加入cache字典中
            node = DLinkedNode(key, value)
            self.add_to_head(node)
            self.cache[key] = node
            self.size += 1
            # 判断数量是否超过容量
            if self.size > self.capacity:
                removed = self.remove_tail()  # 删除双向链表中的最后一个node
                self.cache.pop(removed.key)  # 删除字典cache中的key-node对
                self.size -= 1

    def add_to_head(self, node):
        # 等号左边是位置，右边是node，注意顺序
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        # 等号左边是位置，右边是node
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        # 获得末尾node
        node = self.tail.prev
        # 等号左边是位置，右边是node
        self.tail.prev = node.prev
        node.prev.next = self.tail
        return node  # 返回该node，用于删除字典中对应的key-value


if __name__ == "__main__":
    pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
