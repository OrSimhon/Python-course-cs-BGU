from Stack import Stack


class Linked_List_using_Stack:
    def __init__(self):
        self.stack = Stack()
        self.len = 0

    def __len__(self):
        return self.len

    def __repr__(self):
        help_stack = Stack()
        out = ''
        while self.stack.is_empty() is False:
            tmp = self.stack.pop()
            help_stack.push(tmp)
            out += '[' + str(tmp) + ']' + '->'
        while help_stack.is_empty() is False:
            self.stack.push(help_stack.pop())
        return out

    def add_at_start(self, val):
        self.stack.push(val)
        self.len += 1

    def insert(self, val):
        self.stack.push(val)
        self.len += 1

    def insert(self, val, loc):
        if not (0 <= loc <= self.len):
            print("Invalid index")
            return
        help_stack = Stack()
        while loc > 0:
            help_stack.push(self.stack.pop())
            loc -= 1
        self.stack.push(val)
        while help_stack.is_empty() is False:
            self.stack.push(help_stack.pop())
        self.len += 1

    def delete(self, loc):
        if not (0 <= loc < len(self)):
            print("Invalid index")
            return
        help_stack = Stack()
        while loc > 0:
            help_stack.push(self.stack.pop())
            loc -= 1
        self.stack.pop()
        while help_stack.is_empty() is False:
            self.stack.push(help_stack.pop())

    def __getitem__(self, loc):
        if not (0 <= loc < len(self)):
            print("Invalid index")
            return
        help_stack = Stack()
        while loc > 0:
            help_stack.push(self.stack.pop())
            loc -= 1
        res = self.stack.pop()
        self.stack.push(res)
        while help_stack.is_empty() is False:
            self.stack.push(help_stack.pop())
        return res


lst_use_stack = Linked_List_using_Stack()
lst_use_stack.add_at_start(5)
lst_use_stack.add_at_start(6)
lst_use_stack.add_at_start(7)
lst_use_stack.add_at_start(8)

print(lst_use_stack)

lst_use_stack.insert(15,2)
print(lst_use_stack)

lst_use_stack.delete(4)
print(lst_use_stack)
