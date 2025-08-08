# 单链表个人测试
# 为了进一步学习使用下python继承相关的面向对象特点
# 红茶半两酒
# 2025/08/08
# -*- coding: utf-8 -*-

# ========== 节点基类 ==========
# 单向节点
class Node():
    def __init__(self, item):
        super().__init__(item)
        self.item = item
        self.next = None

# 双向节点
class DoubleNode(Node):
    def __init__(self, item):
        super().__init__(item)  # 调用父类的__init__方法。
        self.prev = None
        self.next = None

# ========== 链表基类 ==========
class BaseLinkedList:
    """链表基类：封装通用方法"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        count = 0
        for _ in self:  # 用迭代器遍历
            count += 1
        return count

    def search(self, item):
        for node in self:
            if node.item == item:
                return True
        return False

    def __iter__(self):
        """迭代器方法，子类必须重写"""
        raise NotImplementedError
        # 这儿就是一个提醒，意思是父类没有实现这个方法


# ========== 单向链表 ==========
class SingleLinkedList(BaseLinkedList):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        cur = self._head
        while cur:
            yield cur
            # 类似于return cur，但是可以保存记忆，同时可以节省内存
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for _ in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur:
            if cur.item == item:
                if pre is None:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            pre = cur
            cur = cur.next
        return False


# ========== 单向循环链表 ==========
class SingleCircularLinkedList(SingleLinkedList):
    def __iter__(self):
        """循环链表迭代器"""
        if self.is_empty():
            return
        cur = self._head
        while True:
            yield cur
            cur = cur.next
            if cur == self._head:  # 回到起点就停
                break

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = self._head

    def remove(self, item):
        if self.is_empty():
            return False
        cur = self._head
        pre = None
        while True:
            if cur.item == item:
                if cur == self._head:
                    # 找到尾节点
                    tail = self._head
                    while tail.next != self._head:
                        tail = tail.next
                    if self._head == self._head.next:
                        self._head = None
                    else:
                        self._head = self._head.next
                        tail.next = self._head
                else:
                    pre.next = cur.next
                return True
            pre = cur
            cur = cur.next
            if cur == self._head:
                break
        return False


# ========== 双向链表 ==========
class DoubleLinkedList(BaseLinkedList):
    def __init__(self):
        super().__init__()

    def __iter__(self):
        cur = self._head
        while cur:
            yield cur
            cur = cur.next

    def add(self, item):
        node = DoubleNode(item)
        node.next = self._head
        if self._head:
            self._head.prev = node
        self._head = node

    def append(self, item):
        node = DoubleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            node = DoubleNode(item)
            cur = self._head
            for _ in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node

    def remove(self, item):
        cur = self._head
        while cur:
            if cur.item == item:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self._head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False


# ========== 测试 ==========
if __name__ == "__main__":
    print("=== 单向链表 ===")
    sll = SingleLinkedList()
    sll.append(1)
    sll.append(2)
    sll.add(0)
    for node in sll:
        print(node.item)

    print("\n=== 单向循环链表 ===")
    scll = SingleCircularLinkedList()
    scll.append(1)
    scll.append(2)
    scll.add(0)
    for node in scll:
        print(node.item)

    print("\n=== 双向链表 ===")
    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.add(0)
    for node in dll:
        print(node.item)
