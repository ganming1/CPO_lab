from mutable import *

class SignLinklist:
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

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    # Add Node
    def append(self, obj):
        node = SignLinklist.Node(obj)
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
        return self.LinklistIterator(self.head)

    # print Call print list
    def __repr__(self):
        return '<' + ','.join(map(str, self)) + '>'


# # Hash table is similar to collection

class ImHashTable(HashTable):
    # def __init__(self, size = 10, list = None):
    #     self.size = size
    #     self.T = [SignLinklist() for x in range(self.size)]
    #     if (list):
    #         self.list_to_hashTable(list)








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

    def im_insert(self, k):
        i = self.hash(k)
        t2 = HashTable(10, self.hashTable_to_list())
        if t2.find(k):
            # print('Duplicated Insert')
            return self
        else:
            t2.T[i].append(k)
            return self

    def delete(self, k):
        t2 = ImHashTable(10,self.hashTable_to_list())
        i = k % t2.size
        for j in t2.T[i]:
            if j == k and j == t2.T[i].head.item:
                t2.T[i].head = t2.T[i].head.next
                break
            if j == k and j == t2.T[i].tail.item:
               pre = t2.T[i].head
               while pre.next != t2.T[i].tail:
                   pre = pre.next
               t2.T[i].tail = None
               pre.next = None
               t2.T[i].tail = pre
               break
            else:
                pre = t2.T[i].head
                print(type(pre.next))
                while pre.next.item != k:
                    pre = pre.next
                if pre.next.item == k:
                    pre.next = pre.next.next
                    break
        return self

    def mconcat(self, ha):
        h1 = HashTable(10, self.hashTable_to_list())
        for i in range(ha.size):
            for j in ha.T[i]:
                h1.insert(j)
        return self

    def reduce(self, f, initial_state):
        state = initial_state
        for i in range(self.size):
            if(self.T[i]):
                current = self.T[i].head
                while current is not None:
                    state = f(state, current.item)
                    current = current.next
        return state

    def map(self, f):
        h1 = HashTable(10, self.hashTable_to_list())
        for i in range(h1.size):
            current = SignLinklist.Node(h1.T[i].head.item)
            while current:
                h1.T[i].head.item = f(current.item)
                current = current.next
        return self

    def find(self, k):
        i = self.hash(k)
        return self.T[i].find(k)

if __name__ == '__main__':
    ht = ImHashTable(3,[1, 2, 3])
    print('\n'.join(map(str, ht.T)))
    # ht=ht.delete(1)
    print(ht.itm_size())
    # print(ht.hashTable_to_list())

