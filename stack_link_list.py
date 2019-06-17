class Node:
    def __init__(self,val):
        self.next = None
        self.data = val

class LinkList:

    def __init__(self):
        self.node = None
        self.prev =None


    def Display(self):
        tmp = self.node
        while self.node != None:
            print(self.node.data)
            self.node = self.node.next

        self.node = tmp

    def Add_stack(self,val):
        if self.node is None:
            self.node = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.node
            self.node = new_node

    def pop_statck(self):
        if self.node is None:
            raise Exception("empty stack")
        data = self.node.data
        self.node = self.node.next
        return data






l = LinkList()
l.Add_stack(1)
l.Add_stack(2)
l.Add_stack(3)
l.Add_stack(4)
l.Add_stack(5)
l.Add_stack(6)
l.Display()
print(l.pop_statck())
print(l.pop_statck())
print(l.pop_statck())
print(l.pop_statck())
print(l.pop_statck())
print(l.pop_statck())
l.Display()