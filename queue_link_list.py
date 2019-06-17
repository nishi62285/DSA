class Node:
    def __init__(self,val):
        self.next = None
        self.data = val

class LinkList:

    def __init__(self):
        self.head = None
        self.node = None


    def Display(self):
        tmp = self.head
        while self.head != None:
            print(self.head.data)
            self.head = self.head.next

        self.head = tmp

    def Add_queue(self,val):
        if self.node is None:
            self.node= Node(val)
            self.head = self.node
        else:
            new_node = Node(val)
            self.node.next = new_node
            self.node = new_node


    def dequeue(self):
        if self.head is None:
            raise Exception("Empty Queue")
        data = self.head.data
        self.head = self.head.next
        return data



l = LinkList()
l.Add_queue(1)
l.Add_queue(2)
l.Add_queue(3)
l.Add_queue(4)
l.Add_queue(5)
l.Add_queue(6)
#l.Display()
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
print(l.dequeue())
#l.Display()