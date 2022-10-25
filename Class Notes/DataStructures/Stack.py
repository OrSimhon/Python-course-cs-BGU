"""
LIFO - Last In First Out
We want our stack to support the following methods:
    push(val)
    pop()
    peek()
    len(my_stack_object)
    my_stack_object.is_empty()
"""


class Stack:
    def __init__(self):
        self.stack_vals = []

    def push(self, val):
        self.stack_vals.append(val)

    def pop(self):
        if self.is_empty():
            return None
        res = self.stack_vals[-1]
        self.stack_vals = self.stack_vals[:-1]
        return res

    def __len__(self):
        return len(self.stack_vals)

    def __repr__(self):
        out = '|'
        for i in range(len(self)):
            out += str(self.stack_vals[i]) + ' '
        out += '<--top'
        return out

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_vals[-1]

    def is_empty(self):
        return len(self) == 0


my_stack = Stack()
my_stack.push(3)
my_stack.push(5)
my_stack.push(7)
print(my_stack)
print(my_stack.is_empty())
print(my_stack.pop())
print(my_stack)
