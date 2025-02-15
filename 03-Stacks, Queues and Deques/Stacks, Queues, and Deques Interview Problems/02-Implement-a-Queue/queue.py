class Queue():
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
       return len(self.items)


q=Queue()

print(q.isEmpty())

q.enqueue('hola')

print(q.size())

q.enqueue('adios')

q.dequeue()
    
print(q.size())