# Node class
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)


# Iterable linked list
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


class SignLinklist:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    # add node
    def append(self, obj):
        node = Node(obj)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Add nodes in bulk
    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    # Find node
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    # Traverse linked list
    def __iter__(self):
        return LinklistIterator(self.head)

    # print Call print list
    def __repr__(self):
        return '<' + ','.join(map(str, self)) + '>'


# Hash table is similar to collection
class HashTable:
    def __init__(self, size=10, list=None):
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

    # the insert function is add_to_tail
    def insert(self, k):
        i = self.hash(k)
        if self.find(k):
            return self
        else:
            self.T[i].append(k)
            return self

    def delete(self, k):
        i = k % self.size
        for j in self.T[i]:
            if j == k and j == self.T[i].head.item:
                self.T[i].head = self.T[i].head.next
                break
            if j == k and j == self.T[i].tail.item:
                pre = self.T[i].head
                while pre.next != self.T[i].tail:
                    pre = pre.next
                self.T[i].tail = None
                pre.next = None
                print('\n'.join(map(str, ht.T)))
                self.T[i].tail = pre
                break
            else:
                pre = self.T[i].head
                print(type(pre.next))
                while pre.next.item != k:
                    pre = pre.next
                if pre.next.item == k:
                    pre.next = pre.next.next
                    break
        return self

    def mconcat(self, ha):
        for i in range(ha.size):
            for j in ha.T[i]:
                self.insert(j)
        return self

    def reduce(self, f, initial_state):
        state = initial_state
        for i in range(self.size):
            if (self.T[i]):
                current = self.T[i].head
                while current is not None:
                    state = f(state, current.item)
                    current = current.next
        return state

    def map(self, f):
        for i in range(self.size):
            current = Node(self.T[i].head.item)
            while current:
                self.T[i].head.item = f(current.item)
                current = current.next
        return self

    def find(self, k):
        i = self.hash(k)
        return self.T[i].find(k)
