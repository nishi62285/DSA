#ip=[15,23,45,67,4,87]
#ip=[8,7,9,10,3,4,1,12,6,5]
ip=[5,14,23,32,41,87,90,50,64,53,43,18]
pq=[]

def Add():
    for i,val in enumerate(ip):
        pq[i]=val
        isLess = True
        while isLess == True:
            parent = float((i - 1) / 2)
            if parent >=0 and pq[int(parent)] > val:
                tmp = pq[int(parent)]
                pq[int(parent)] = val
                pq[int(i)] = tmp
                i = parent
            else:
                isLess = False


def Add(element):
        pq.append(element)
        isLess = True
        val = element
        i = len(pq)-1
        while isLess == True:
            parent = float((i - 1) / 2)
            if parent >=0 and pq[int(parent)] > val:
                tmp = pq[int(parent)]
                pq[int(parent)] = val
                pq[int(i)] = tmp
                i = parent
            else:
                isLess = False
def empty():
    return len(pq)==0

def Remove():
    if len(pq)==0:
        return None
    pop_val = pq[0]
    print(pop_val)
    pq[0] = 0
    i = 0
    isDone = True
    lastIndex = len(pq)-1
    check = pq.pop()
    while isDone == True:
        child1 = 2 * i + 1
        child2 = 2 * i + 2
        min_index=0
        if i == len(pq)-1 or child1 > len(pq)-1:
            break
        if child2 > len(pq)-1:
            min_index = child1
        elif pq[child1] < pq[child2]:
            min_index=child1
        else:
            min_index = child2
        if check > pq[min_index]:
            tmp = pq[min_index]
            pq[min_index] = check
            pq[i] = tmp
            lastIndex = lastIndex -1
            i =min_index
        else:
            isDone = False
    return pop_val    

def Display():
    print(pq)


def DecreaseKey(index,value):
    pq[index] = pq[index]-value
    check = pq[index]
    isDone = True
    while isDone == True:
        parent = float((index -1) /2)
        if check < pq[int(parent)]:
            tmp = pq[int(parent)]
            pq[int(parent)] = check
            pq[index]=tmp
            index = int(parent)
        else:
            isDone = False

def IncreaseKey(index,value):
    pq[index] = pq[index] + value
    check = pq[index]
    isDone = True
    while isDone == True:
        child1 = 2 * index + 1
        child2 = 2 * index + 2
        min_index = 0
        if index == len(pq) - 1 or child1 > len(pq) - 1:
            break
        if child2 > len(pq) - 1:
            min_index = child1
        elif pq[child1] < pq[child2]:
            min_index = child1
        else:
            min_index = child2
        if check > pq[min_index]:
            tmp = pq[min_index]
            pq[min_index] = check
            pq[index] = tmp
            index =min_index
        else:

            isDone = False

for i in [18,2]:
    Add(i)

while not empty():
    print(Remove())

#IncreaseKey(1,20)
#DecreaseKey(4,20)

##Add()
#Remove()
#Remove()
#Remove()
#Display()
