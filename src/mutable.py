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

    # add node
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

    def insert(self, k):
        i = self.hash(k)
        if self.find(k):
            # print('Duplicated Insert')
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

    def reduce(self, sum):
        result = 0
        for i in range(self.size):
            for j in self.T[i]:
                result += j
        return result



    def find(self, k):
        i = self.hash(k)
        return self.T[i].find(k)

if __name__ == '__main__':
    ht = HashTable()
    ht.insert(1)
    ht.insert(11)
    ht.insert(21)
    ht.insert(18)
    # ht.insert(29)
    # ht.insert(28)
    # ht.insert(38)
    # ht.insert(219)
    ht1 = HashTable(10,[1, 32, 5, 67, 8])
    # ht.mconcat(ht1)
    print('\n'.join(map(str, ht.T)))
    print(ht.reduce("sum"))

#     print('\n'.join(map(str, ht.T)))
#
#     print(ht.find(210))
#     print('\n'.join(map(str, ht.T)))
    # ht.delete(1)
    # ht.delete(28)
    # print('\n'.join(map(str, ht.T)))


    # ls = ht.hashTable_to_list()
    #
    # print(ls)
    # print(ht.itm_size())
    #
    # ht2 = HashTable()
    # ht2.list_to_hashTable([1,2,4,5,10,20,45])
    # ls2 = ht2.hashTable_to_list()
    # print(ls2)

