class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 雜湊表：key -> ListNode
        
        # 建立虛擬頭尾節點，方便操作
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    # 將節點移動到雙向鏈結串列的最前面（表示最近被使用）
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node_to_head(node)

    # 移除某個節點
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # 將節點新增到虛擬頭節點的後面
    def _add_node_to_head(self, node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    # 移除最久未使用的節點（即虛擬尾節點的前一個節點）
    def _pop_tail(self):
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 有被讀取，代表最近被使用過，移動到頭部
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 如果 key 已經存在，更新值並移動到頭部
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 如果 key 不存在，建立新節點
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_node_to_head(new_node)
            
            # 檢查是否超出容量
            if len(self.cache) > self.capacity:
                # 移除最尾端的節點 (LRU)
                lru_node = self._pop_tail()
                # 記得也要從雜湊表中刪除
                del self.cache[lru_node.key]