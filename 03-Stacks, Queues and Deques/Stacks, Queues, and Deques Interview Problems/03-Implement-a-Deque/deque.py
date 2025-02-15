class Deque(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.itmes==[]
    
    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
d= Deque()

d.addFront(1)
d.addRear(0)

print(d.size())
d.removeFront()
d.removeRear()

print(d.size())

    
