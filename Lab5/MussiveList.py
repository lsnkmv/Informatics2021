class MussiveList:
    items = []

    def cteateList(self, count):
        self.items = [None for i in range(count)]
        self.size = count

    def destroyList(self):
        self.items = []
    
    def isEmpty(self):
        if self.items == [] or self.items == [None for i in range(self.size)] :
            print('The list is empty')
        else:
            print('The list is not empty')

    def insert(self, index, new_element):
        self.items[index] = new_element
    
    def remove(self, index):
        self.items[index] = None

    def retrive(self, index):
        if self.items[index]:
            return self.items[index]
        else:
            return 'No such element'
    
    def getLength(self):
        count = 0
        for el in self.items:
            if el:
                count += 1
        return count

    def find(self, element):
        if element in self.items:
            return self.items.index(element)
        else:
            return 'No such element'


