def readfile(x):
    list2=[]
    f=open(x,'r')
    list1=f.readlines()
    for line in list1:
        row=[]
        for character in range(len(line)-1):
            row.append(int(line[character]))
        list2.append(row)
    return list2

def process(listoflists):
    count=[]
    idxpts=[]
    for idx1 in range(len(listoflists)):
        for idx2 in range(len(listoflists[idx1])):
            if idx1==0 and idx2==0:
                if (listoflists[idx1][idx2]<listoflists[idx1+1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2+1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx1==len(listoflists)-1 and idx2==0:
                if (listoflists[idx1][idx2]<listoflists[idx1-1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2+1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx1==0 and idx2==len(listoflists[0])-1:
                if (listoflists[idx1][idx2]<listoflists[idx1+1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2-1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx1==len(listoflists)-1 and idx2==len(listoflists[0])-1:
                if (listoflists[idx1][idx2]<listoflists[idx1-1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2-1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx1==0:
                if (listoflists[idx1][idx2]<listoflists[idx1+1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2+1]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2-1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx1==len(listoflists)-1:
                if (listoflists[idx1][idx2]<listoflists[idx1-1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2+1]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2-1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx2==0:
                if (listoflists[idx1][idx2]<listoflists[idx1-1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1+1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2+1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            elif idx2==len(listoflists[0])-1:
                if (listoflists[idx1][idx2]<listoflists[idx1-1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1+1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2-1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
            else:
                if (listoflists[idx1][idx2]<listoflists[idx1-1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1+1][idx2]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2+1]) and (listoflists[idx1][idx2]<listoflists[idx1][idx2-1]):
                    count.append(listoflists[idx1][idx2])
                    idxpts.append([idx1,idx2])
    count1=[x+1 for x in count]
    return sum(count1),idxpts

def neighbours(a,l,indices):
    i,j=l[0],l[1]
    flag=1
    if i!=len(a)-1:
        if a[i+1][j]>a[i][j] and a[i+1][j]!=9 and [i+1,j] not in indices:
            indices.append([i+1,j])
            flag+=neighbours(a,[i+1,j],indices)
    if i!=0:
        if a[i-1][j]>a[i][j] and a[i-1][j]!=9 and [i-1,j] not in indices:
            indices.append([i-1,j])
            flag+=neighbours(a,[i-1,j],indices)
    if j!=len(a[0])-1:
        if a[i][j+1]>a[i][j] and a[i][j+1]!=9 and [i,j+1] not in indices: 
            indices.append([i,j+1])
            flag+=neighbours(a,[i,j+1],indices)
    if j!=0:
        if a[i][j-1]>a[i][j] and a[i][j-1]!=9 and [i,j-1] not in indices:
            indices.append([i,j-1])
            flag+=neighbours(a,[i,j-1],indices)
    return flag

def process2(input,lowpts):
    sizes=[]
    for pt in lowpts:
        count=0
        count+=neighbours(input,pt,indices=[])
        sizes.append(count)
    product=1
    #print(sizes)
    for i in range(3):
        product*=max(sizes)
        sizes.remove(max(sizes))
    return product

input=readfile('Day9_2021_input.txt')
ansx,points=process(input)
ans=process2(input,points)
print(ans)


