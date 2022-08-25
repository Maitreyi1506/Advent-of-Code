def readinput(f):
    fh=open(f,'r')
    lnum=[]
    l=fh.readline().split(' ')
    for i in l:
        lnum.append(int(i))
    fh.close()
    return lnum

cdx=[]
def readnode(a,pos):
    #should return last position for node
    #should also return sum of metadata
    nc=a[pos]
    nm=a[pos+1]
    cidx=pos+2
    sum=0
    for i in range(nc):
        idx,csum=readnode(a,cidx)
        sum+=csum
        cidx=idx+1
    for j in range(nm):
        sum+=a[cidx+j]
    return cidx+j, sum


def readnode2(a,pos):
    #should return last position for node
    #should also return sum of metadata
    nc=a[pos]
    nm=a[pos+1]
    cidx=pos+2
    sum=0
    children=[]   #stores values of children
    for i in range(nc):     
        idx,csum=readnode2(a,cidx)
        children.append(csum)
        cidx=idx+1
    if nc==0:
        for j in range(nm):
            sum+=a[cidx+j]
    else: 
        for j in range(nm):
            childidx=a[cidx+j]
            if childidx<=nc:
                sum+=children[childidx-1]
            else:
                pass
    return cidx+j, sum

#def check(a):
    for j in range(10):
        cdx.append(0)
    p=len(cdx)-10
    for idx in range(p):
        y=cdx[idx]
        if y>0:
            for i in range(a[y]):
                l=idx+i
                cdx.pop(l)
    return cdx

#def value(a,pos):
    nm=a[pos+1]
    nc=a[pos]
    sum=0
    if nc==0:
        for i in range (nm):
            sum+=a[index-i]
    else:
        for i in range(nc):
            if (a[index-i]<=nc):
                ydx=check(a)
                for x in ydx:
                    if x>0:
                        sum+=value(a,x)
    return sum

#def value(a):
    children=a[0]
    metadata=a[1]
    nc=len(children)
    #if no children, value=sum of metadata
    if nc==0:
        return sum(metadata)
    #if children, value= values of children with metadata indices
    else:
        total=0
        for child in metadata:
            if child<=nc:
                total+=value(children[child-1])
        return total


#write a function that returns a on entering sample
#def converttotree(list,idx):
    children=[]
    metadata=[]
    list[idx]
    list[idx+1]=len(metadata)
    cidx=idx+2
    for i in range(len(children)):
        childtree,idx2=converttotree(list,cidx)
        children.append(childtree)
        cidx+=idx2
    for j in range(len(metadata)):
        cidx+=j
        metadata.append(list[cidx])
    tree=[children,metadata]
    return tree, cidx

myinput=readinput('2018_8_input.txt')

#sample=[2, 3, 0, 3, 10, 11, 12, 1,1, 0, 1, 99, 2, 1, 1, 2]
#a=[[b,c],[1,1,2]]
#b=[[],[10,11,12]]
#c=[[d],[2]]
#d=[[],[99]]
#a=[[[[],[10,11,12]],[[[[],[99]]],[2]]],[1,1,2]]
print(readnode2(myinput,0))
#index,total=readnode2(sample,0)
#print(index,total)
#print(converttotree(sample,0))
#print(a)