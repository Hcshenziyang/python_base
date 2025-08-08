# 单链表个人测试
# 插入和删除的逻辑有点复杂，感觉有更优解，看视频了，没有自己写
# 红茶半两酒
# 2025/08/07

# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head == None

    def length(self):
        num = 0
        temp = self._head
        while temp != None:
            temp = temp.next
            num += 1
        return num

    def travel(self):
        temp = self._head
        while temp != None:
            print(temp.item)
            temp = temp.next
        print('')

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            temp = self._head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def insert(self, pop, item):
        if pop < 0:
            print("位置属性为负，已自动执行尾部插入！")
            self.append(item)
            return 0

        node = Node(item)
        temp = self._head
        if self.length() < pop:
            print("插入节点超出链表长度！！")
        elif self.is_empty():
            self._head = node
        else:
            temp = self._head
            for i in range(0, pop-1):
                temp = temp.next
            temp1 = temp.next
            temp.next = node
            node.next = temp1

    def remove(self, item):
        temp = self._head
        if temp.item == item:
            self._head = temp.next
            return 1
        pre = None
        while temp != None:
            if temp.item == item:
                pre.next = temp.next
                break
            pre = temp
            temp = temp.next


    def search(self, item):
        temp = self._head
        while temp != None:
            if temp.item == item:
                return True
            temp = temp.next
        return False
