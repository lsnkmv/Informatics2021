class ListStack:
    def create_Stack(self, max_count):
        self.items = list()
        self.max_count = max_count
        self.count = 0

    def destroy_Stack(self):
        self.items = list()
        self.max_count = 0
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def s_push(self, new_el):
        if self.count < self.max_count:
            self.count += 1
            self.items.append(new_el)
            return True
        return False

    def s_pop(self, new_el):
        if len(self.items) > 0:
            self.count -= 1
            return self.items.pop()
        return ("No elements in Stack!")

    def get_top(self):
        return self.items[self.count-1]