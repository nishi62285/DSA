class Node:
    def __init__(self,val):
        self.next = None
        self.data = val

class LinkList:

    def __init__(self):
        self.node = None


    def get_coefficient(self,expr):
        if len(expr) > 1:
            return expr[:-1]
        elif expr in ['+','-']:
            return  expr
        return 1

    def get_polynomial(self,expr,expr1):
        if expr is not None:
            return expr.data[-1:]
        elif expr1 is not None:
            return expr1.data[-1:]

    def Add(self,val):
        tmp = self.node
        if self.node is None:
            self.node=Node(val)
        else:
            while self.node.next != None:
                self.node=self.node.next
            self.node.next=Node(val)
            self.node=tmp

    def is_operator(self,expr):
        if expr in ['+','-']:
            return expr
        return None

    def compute(self,op1,op2,node_data,l2_data):
        return eval((op2 if op2 is not None else '+') + '+' + (node_data if node_data is not None else '0') + (
        op1 if op1 is not None else '+') + (l2_data if l2_data is not None else '0'))

    def AddPolynomial(self,l2):
        tmp = self.node
        tmp1=l2
        result=""
        operator_stack=[]
        node_data=None
        l2_data=None
        if self.node is None or l2 is None:
            raise Exception("empty")
        while self.node != None or l2 != None:
            if self.node is not None:
                node_data = self.get_coefficient(self.node.data)
            else:
                node_data=None
            if l2 is not None:
                l2_data=self.get_coefficient(l2.data)
            else:
                l2_data=None

            if self.is_operator(node_data) or self.is_operator(l2_data):
                operator_stack.append(node_data)
                operator_stack.append(l2_data)
                if self.node is not None:
                    self.node=self.node.next
                if l2 is not None:
                    l2 = l2.next
                continue
            if len(operator_stack)==0:
                expr = self.compute('+','+',node_data,l2_data)
                result = result + str(expr) + self.get_polynomial(self.node,l2)
            else:
                op1=operator_stack.pop()
                op2=operator_stack.pop()
                expr = self.compute(op1,op2,node_data,l2_data)
                if '-' not in str(expr):
                    expr='+'+str(expr)
                result = result + str(expr) + self.get_polynomial(self.node,l2)
            if self.node is not None:
                self.node=self.node.next
            if l2 is not None:
                l2 = l2.next

        self.node =tmp
        l2=tmp1
        print(result)

    def Display(self):
        tmp = self.node
        while self.node != None:
            print(self.node.data)
            self.node=self.node.next
        self.node=tmp


l=LinkList()
l.Add('1x')
l.Add('+')
l.Add('1y')
l.Display()

l1=LinkList()
l1.Add('1x')
l1.Add('+')
l1.Add('1y')
l1.Add('+')
l1.Add('1z')
l1.Display()

l.AddPolynomial(l1.node)
l.AddPolynomial(l1.node)