class Node:
    def __init__(self,score,char):
        self.score=score
        self.char=char

pq=[]
input='MAHARASHTRA'
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
print(sortedop)

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
    #pq[0]=None
    #pq[0].score=0
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

            # if len(pq)>0:
            #     #pass
            #     pq[0]=check
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





# def merge(pq):
#      if len(pq) == 1:
#          return pq[0]
#      else:
#         a=Remove()
#         b=Remove()
#         totalScore= a.score+b.score
#         totalChar=a.char+b.char
#         Add(Node(totalScore,totalChar))
#         merge(pq)

stck=[]

# while len(pq)>1:
#     a=Remove(pq)
#     b=Remove(pq)
#     stck.append(a.char)
#     stck.append(b.char)
#     totalScore = a.score + b.score
#     totalChar = a.char + b.char
#     #stck.append(totalChar)
#     Add(Node(totalScore,totalChar))
#     ss=pq

def rec():
    if len(pq)==1:
        return
    else:
        a=Remove(pq)
        b=Remove(pq)
        stck.append(str(a.char) + '-' + str(a.score))
        stck.append(str(b.char) + '-' + str(b.score))
        totalScore = a.score + b.score
        totalChar = a.char + b.char
        #stck.append(totalChar)
        Add(Node(totalScore,totalChar))
        return
        rec()

rec()

while len(stck)>1:
    print(stck.pop())

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
