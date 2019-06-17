class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


class LinkList:

    def __init__(self):
        self.head_val = 0
        self.node=None
        self.tail = self.node
        self.head = self.node

    def AddLeft(self, val):
        new_node = Node(val)
        if self.node is None:
            self.node = new_node
            self.head = self.node
        else:
            self.head.prev=new_node
            new_node.next = self.head
            self.head = new_node
            a=1

    def AddRight(self,val):
        new_node = Node(val)
        if self.node is None:
            self.node = new_node
            self.tail = self.node
        elif self.tail is None:
            self.tail = self.node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            b=1

    def RemoveFromLeft(self):
        tmp =self.head
        if self.head is None:
            raise Exception("Empty")
        elif self.head.next is None:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev=None
        a=1

    def RemoveFromRight(self):
        tmp = self.tail
        if self.tail is None:
            raise Exception("Empty")
        elif self.tail.prev is None:
            self.tail = None
            self.head=None
            return
        self.tail= self.tail.prev
        self.tail.next = None
        a = 1

    def DisplayFromLeft(self):
        tmp = self.head

        while self.head != None:
            print(self.head.data)
            self.head=self.head.next

        self.head = tmp

    def DisplayFromRight(self):
        tmp = self.tail

        while self.tail != None:
            print(self.tail.data)
            self.tail=self.tail.prev

        self.tail = tmp

l= LinkList()
l.AddLeft(1)
l.AddLeft(2)
l.AddLeft(3)
l.AddLeft(4)
# l.DisplayFromLeft()
# l.RemoveFromLeft()
# l.RemoveFromLeft()
# l.RemoveFromLeft()
# l.DisplayFromLeft()
l.AddRight(5)
l.AddRight(6)
l.AddRight(7)
l.AddRight(8)
#l.DisplayFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
l.RemoveFromRight()
# l.RemoveFromLeft()
# l.RemoveFromLeft()
#l.RemoveFromRight()
#l.RemoveFromRight()
#l.DisplayFromRight()
#l.DisplayFromLeft()




