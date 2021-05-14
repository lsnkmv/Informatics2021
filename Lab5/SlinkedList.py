class SLinkedList:

    def cteateList(self):
        self.headval = None

    def insert(self, new_element):
        new_node = NodeLinked(new_element)
        if not self.headval:
            self.headval = new_node
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = new_node
    
    def remove(self, remove_element):
        head = self.headval
        if not head:
            if head.dataval == remove_element:
                self.headval = head.nextval
                head = None
                return
        while not head:
            if head.dataval == remove_element:
                break
            prev = head
            head = head.nextval
        if head == None:
            return
        prev.nextval = head.nextval
        head = None

    def retrive(self, index):
        i = 0
        finder = 'no such element'
        head = self.headval
        if not head:
            while head is not None:
                i += 1
                if i == index:
                    finder = head.dataval
        return finder
    
    def find(self, element):
        i = 0
        finder = 'no such element'
        head = self.headval
        if not head:
            while head is not None:
                i += 1
                if head.dataval == element:
                    finder = i
        return finder

class NodeLinked:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None