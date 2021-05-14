class StackNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedStack:
    
    def __init__(self):
        self.top = None
        self.size = 0

    def destroy(self):
        while not self.is_empty:
            self.pop()

    def is_empty(self):
        return self.top == None

    def push(self, new_el):
        node = StackNode(new_el)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1
        return new_el

    def pop(self, element = None):
        if self.is_empty(): 
            return None
        else:
            top = self.top.data
            self.top = self.top.next
            self.size -= 1
            return top


    def get_top(self):
        if not self.is_empty():
            return self.top.data