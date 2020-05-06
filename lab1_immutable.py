class SignLinklist:
    # 节点类
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

        def __str__(self):
            return str(self.item)

    # 可迭代链表类
    class LinklistIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    # 添加节点
    def append(self, obj):
        node = SignLinklist.Node(obj)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # 批量添加节点
    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    # 查找节点
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    # 遍历链表
    def __iter__(self):
        return self.LinklistIterator(self.head)

    # print 调用打印链表
    def __repr__(self):
        return '<' + ','.join(map(str, self)) + '>'


# 哈希表 类似于集合
class HashTable:
    # def __init__(self, size = 10, list = None):
    #     self.size = size
    #     self.T = [SignLinklist() for x in range(self.size)]
    #     if (list):
    #         self.list_to_hashTable(list)

    def __init__(self, size = 10, list = None):
        self.size = size
        self.T = [SignLinklist() for x in range(self.size)]
        if (list):
            self.list_to_hashTable(list)


    def size(self):
        return self.size

    def itm_size(self):
        s = 0
        for i in range(self.size):
            for j in self.T[i]:
                s += 1
        return s

    def hash(self, k):
        return k % self.size

    def hashTable_to_list(self):
        lst = []
        for i in range(self.size):
            for j in self.T[i]:
                lst.append(j)
        return lst

    def list_to_hashTable(self, lst):
        for i in range(len(lst)):
            self.insert(lst[i])

    def insert(self, k):
        i = self.hash(k)
        t2 = HashTable(self.hashTable_to_list())
        if t2.find(k):
            # print('Duplicated Insert')
            return self
        else:
            t2.T[i].append(k)
            return self

    # def delete(self, k):
    #     t2 = HashTable(self.hashTable_to_list())
    #     i = k % t2.size
    #     for j in t2.T[i]:
    #         if j == k and j == t2.T[i].head.item:
    #             t2.T[i].head = t2.T[i].head.next
    #             break
    #         if j == k and j == t2.T[i].tail.item:
    #            pre = t2.T[i].head
    #            while pre.next != t2.T[i].tail:
    #                pre = pre.next
    #            t2.T[i].tail = None
    #            pre.next = None
    #            t2.T[i].tail = pre
    #            break
    #         else:
    #             pre = t2.T[i].head
    #             print(type(pre.next))
    #             while pre.next.item != k:
    #                 pre = pre.next
    #             if pre.next.item == k:
    #                 pre.next = pre.next.next
    #                 break
    #     return self

    def find(self, k):
        i = self.hash(k)
        return self.T[i].find(k)

if __name__ == '__main__':
    t = HashTable(10, [12])

