class Queue:

    def create_Queue(self, max_count):
        self.items = list()
        self.max_count = max_count
        self.count = 0

    def delete_Queue(self):
        self.items = list()
        self.count = 0
        self.max_count = 0

    def en_queue(self, dataval):
        if self.count < self.max_count:
            self.count += 1
            self.items.insert(0,dataval)
            return True
        return False

    def de_queue(self):
        if len(self.items)>0:
            self.count -= 1
            return self.items.pop()
        return ("No elements in Queue!")

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def get_front(self):
        return self.items[self.count-1]