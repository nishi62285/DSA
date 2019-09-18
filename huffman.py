class Node:
    def __init__(self,score,char):
        self.score=score
        self.char=char

pq=[]
input='NISHIKANT ABCD'
count={}
sortedop=[]

def getCount(a):
    if count.get(a) != None:
        count[a] = int(count[a])+1
    else:
        count[a] = 1

for i in input:
    getCount(i)

sortedop=list(count.keys())
sortedop.sort()
#print(sortedop)

def Add(node):
    element=node.score
    pq.append(node)
    isLess = True
    val = element
    i = len(pq) - 1
    while isLess == True:
        parent = float((i - 1) / 2)
        if parent >= 0 and pq[int(parent)].score > val:
            tmp = pq[int(parent)]
            pq[int(parent)] = node
            pq[int(i)] = tmp
            i = parent
        else:
            isLess = False

for j in sortedop:
    score = count.get(j)
    node = Node(score,j)
    Add(node)

def Remove(pq):
    if len(pq)==1:
        nd=Node(pq[0].score,pq[0].char)
        pq.pop()
        return nd
    res=pq[0]
    new_node = Node(res.score,res.char)
    i = 0
    isDone = True
    lastIndex = len(pq)-1
    check = pq.pop()
    pq[0]=check
    while isDone == True:
        child1 = 2 * i + 1
        child2 = 2 * i + 2
        min_index=0
        if i == len(pq)-1 or child1 > len(pq)-1:
            break
        if child2 > len(pq)-1:
            min_index = child1
        elif pq[child1].score <= pq[child2].score:
            min_index=child1
        else:
            min_index = child2
        if check.score >= pq[min_index].score:
            tmp = pq[min_index]
            pq[min_index] = check
            pq[i] = tmp
            lastIndex = lastIndex -1
            i =min_index
        else:
            isDone = False

    return new_node

class TreeNode:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


stck=[]


def rec():
    if len(pq)==1:
        return pq
    else:
        a=Remove(pq)
        b=Remove(pq)
        totalScore = a.score + b.score
        totalChar = a.char + b.char
        stck.append(a.char+ '-'+b.char)
        Add(Node(totalScore,totalChar))
        q=rec()
        return q

a=rec()
print(stck)

def _Add(root,val):
    if root == None:
        pass
    elif ''.join(root.data.split('-'))==''.join(val.split('-')):
        root.left = TreeNode(val.split('-')[0])
        root.right = TreeNode(val.split('-')[1])
        return
    else:
        _Add(root.left,val)
        _Add(root.right,val)
    return root

def GetScore(root,val,i,dict):
    if dict.get(val) != None:
        dict[val] = str(dict[val])+ str(i)
    else:
        dict[val]=i
    if root==None:
        pass
    elif root.data == val:
        return
    else:
        if val in root.left.data:
            GetScore(root.left,val,0,dict)
        else:
            GetScore(root.right, val, 1, dict)
    return root

root= TreeNode(a[0].char)
dict={}
while len(stck) >0:
    i=stck.pop()
    _Add(root,i)

for i in sortedop:
    GetScore(root,i,None,dict)

f = open('C:/Users/ABC/Desktop/Data/op.txt','a')
for i in input:
    f.write(dict.get(i)+'*')

f.write('\n')

for i,j in dict.items():
    f.write(str(i)+'-'+str(j))
    f.write('\n')

f.close()

r = open('C:/Users/ABC/Desktop/Data/op.txt','r')
op=r.readline()

inv_map={v:k for k,v in dict.items()}
str=""
for i in op.split('*'):
    if inv_map.get(i) != None:
        str=str + inv_map.get(i)

print(str)





































#
#
# def Remove():
#     pq[0] = 0
#     i = 0
#     isDone = True
#     lastIndex = len(pq)-1
#     check = pq.pop()
#     while isDone == True:
#         child1 = 2 * i + 1
#         child2 = 2 * i + 2
#         min_index=0
#         if i == len(pq)-1 or child1 > len(pq)-1:
#             if len(pq)>0:
#                 pq[0]=check
#             break
#         if child2 > len(pq)-1:
#             min_index = child1
#         elif pq[child1] < pq[child2]:
#             min_index=child1
#         else:
#             min_index = child2
#         if check > pq[min_index]:
#             tmp = pq[min_index]
#             pq[min_index] = check
#             pq[i] = tmp
#             lastIndex = lastIndex -1
#             i =min_index
#         else:
#             isDone = False
#
