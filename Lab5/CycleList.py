class CycleList:
    def cteateList(self):
        self.headval = None
        self.tailval = None
        self.count = 0

    def insert(self, new_element):
        new_node = NodeCycle(new_element)

        if self.headval is None:
            self.headval = new_node
            self.tailval = new_node
            self.tailval.next = self.headval
        else:
            new_node.next = self.headval
            self.tailval.next = new_node
            self.tailval = new_node
        self.count +=1

    def remove(self, remove_element):
        current = self.headval.next
        previous = self.headval
        checker = self.count

        if self.headval is None:
            return 'The list is empty'
        while current != self.headval:
            if current.dataval == remove_element:
                if previous != None:
                    previous.next = current.next
                    if current == self.tailval:
                        self.tailval = previous
                else:
                    if self.count == 1:
                        self.headval = self.tailval = None
                    else:
                        self.headval = current.next
                        self.tailval.next = current.next
                self.count -= 1
            previous = current
            current = current.next
        if checker == self.count:
            return 'No such element'

    
    def find(self, element):
        current = self.headval
        finder = 'no such element'
        if current == None:
            return finder

        while current is not None:
            if current.dataval == element:
                finder = 'the list contains the {}'.format(element)
                return finder
            current = current.next
        return finder

class NodeCycle:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None