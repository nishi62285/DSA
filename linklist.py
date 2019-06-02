class Node:
    def __init__(self,val):
        self.next = None
        self.data = val

class LinkList:

    def __init__(self):
        self.node = None

    def Add(self,val):
        new_node = Node(val)
        if self.node is None:
            self.node = new_node
        else:
            tmp = self.node
            while self.node.next != None:
                self.node = self.node.next

            self.node.next = new_node
            self.node = tmp

    def Display(self):
        tmp = self.node
        while self.node != None:
            print(self.node.data)
            self.node = self.node.next

        self.node = tmp

    def AddByIndex(self,index,val):
        tmp = self.node
        counter = 0
        while self.node.next != None and counter != index:
            counter = counter + 1
            self.node = self.node.next

        next_node = self.node.next
        new_node = Node(val)
        new_node.next = next_node
        self.node.next = new_node
        self.node = tmp

    def AddAfterValue(self,value,val):
        tmp = self.node
        counter = 0
        while self.node.next != None and self.node.data != value:
            counter = counter + 1
            self.node = self.node.next

        next_node = self.node.next
        new_node = Node(val)
        new_node.next = next_node
        self.node.next = new_node
        self.node = tmp

    def Delete(self,value):
        tmp = self.node
        curr = self.node
        prev = None
        while curr.next != None and curr.data != value:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        self.node = tmp

    def RemoveDuplicate(self):
        ele=[]
        tmp = self.node
        curr = self.node
        prev = None
        while curr.next != None:
            if curr.data not in ele:
                ele.append(curr.data)
            else:
                prev.next = curr.next
            prev = curr
            curr = curr.next

        self.node = tmp

    def Reverse(self):
        prev = None
        curr = self.node

        while curr.next != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr.next = prev
        self.node = curr

    def Union(self,linkList2):
        tmp = self.node
        ele =[]


        while self.node.next != None:
            ele.append(self.node.data)
            self.node = self.node.next

        last_node = self.node
        self.node = tmp

        tmp1 = linkList2.node
        prev=None
        curr = linkList2.node
        while curr != None:
            if curr.data in ele:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr= curr.next
        linkList2 = tmp1
        last_node.next = linkList2

    def Intersection(self,l2):
        pass

l = LinkList()
l.Add(1)
l.Add(2)
l.Add(3)
l.Add(4)
l.Add(5)
l.Add(6)
# l.AddByIndex(2,10)
# l.AddAfterValue(2,20)
# l.Delete(20)
# l.RemoveDuplicate()
# l.Reverse()

l2 = LinkList()
l2.Add(7)
l2.Add(8)
l2.Add(9)
l2.Add(10)
l2.Add(3)
l2.Add(5)
l.Union(l2)
l.Display()



