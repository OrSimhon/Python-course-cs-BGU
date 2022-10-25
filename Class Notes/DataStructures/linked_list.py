import timeit

"""
ADT - Abstract Data Structures
Lists, Dictionaries, Tuples, Strings, Linked lists...

Linked List
Pros & Cons :
Spread in the memory (linked list) vs a chunk of memory (list)
Pointing only from previous member (linked list) vs direct pointing (list)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '[' + str(self.value) + ']'


class Linked_List:
    def __init__(self):
        self.head = None
        self.len = 0

    def __repr__(self):
        out = ''
        p = self.head
        while p is not None:
            out += str(p) + '-->'
            p = p.next
        return out

    def __len__(self):
        return self.len

    def add_at_start(self, val):
        p = Node(val)
        p.next = self.head
        self.head = p
        self.len += 1

    def __getitem__(self, loc):
        if (not (0 <= loc < len(self))) or (not isinstance(loc, int)):
            print("Invalid location")
            return

        p = self.head
        for i in range(loc):
            p = p.next
        return p.value

    def insert(self, loc, val):
        if (not (0 <= loc < self.len)) or (not isinstance(loc, int)):
            print("Invalid location")
            return

        if loc == 0:
            self.add_at_start(val)
            return

        p = self.head
        for i in range(loc - 1):
            p = p.next
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1

    def append(self, val):
        def append_rec(node, val):
            if node.next is None:
                node.next = Node(val)
            else:
                append_rec(node.next, val)

        if self.head is None:
            self.head = Node(val)
        else:
            append_rec(self.head, val)
        self.len += 1

    def print_reversed(self):
        def print_reversed_rec(node):
            if node.next is None:
                print(node)
                return
            print_reversed_rec(node.next)
            print(node)

        if self.head is None:
            print('X->')
        else:
            print_reversed_rec(self.head)

    def accumulated_rec(self):
        """
        O(n)
        :return:
        """

        def accumulated_rec_help(node, res):
            if node.next is None:
                res.add_at_start(node.value)
            else:
                accumulated_rec_help(node.next, res)
                res.add_at_start(node.value + res.head.value)

        res = Linked_List()
        accumulated_rec_help(self.head, res)
        return res

    def accumulated_iter(self):
        """
        O(n^2)
        :return:
        """
        res = Linked_List()
        for i in range(len(self)):
            acc_to_add = 0
            for j in range(i, len(self)):
                acc_to_add += self[j]
            res.append(acc_to_add)
        return res

    def delete(self, loc):
        if (not (0 <= loc < self.len)) or (not isinstance(loc, int)):
            print("Invalid location")
            return

        if loc == 0:
            self.head = self.head.next
            return

        p = self.head
        for i in range(loc - 1):
            p = p.next
        p.next = p.next.next
        self.len -= 1


lnk = Linked_List()
lnk.add_at_start(6)
lnk.add_at_start(4)
lnk.add_at_start(3)
lnk.add_at_start(5)
print(lnk)

lnk.insert(2, 10)
print(lnk)

lnk.delete(2)
print(lnk)

lnk.append(10)
print(lnk)

print("")
lnk.print_reversed()

print(lnk.accumulated_rec())
print(lnk.accumulated_iter())

# Tune comparison
big_link_lst = Linked_List()
for i in range(900):
    big_link_lst.add_at_start(i)

start = timeit.default_timer()
rec_accumulated_lst = big_link_lst.accumulated_rec()
stop = timeit.default_timer()
rec_time = stop-start
print("Recursive Time O(n):   ", rec_time)


start = timeit.default_timer()
iter_accumulated_lst = big_link_lst.accumulated_iter()
stop = timeit.default_timer()
iter_time = stop-start
print("Iterative Time O(n^2): ", iter_time)

print("Recursion was", int(iter_time/rec_time), 'times faster!')
