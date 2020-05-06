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

    def __init__(self, size=10):
        self.size = size
        self.T = [SignLinklist() for x in range(self.size)]

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print('Duplicated Insert')
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)
    # def map_to_list(self):


ht = HashTable()
ht.insert(1)
ht.insert(18)
ht.insert(29)
ht.insert(31)
print(ht)
print(ht.T[1])
print(type(ht.T[1]))
type(ht)
list=[]
# for i in range(ht.size):
#     if(ht.T[i]):
       
        # for j in :
        #     print(j)
        #     list.append(j)
        #     print(j)
        

    
# print(ht)  
# print('\n'.join(map(str, ht.T)))


