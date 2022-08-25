import Day18_2021

def readfile(x):
    f=open(x,'r')
    l=f.readlines()
    retl=[]
    x,y=0,0
    for i in l:
        retl.append(eval(i.rstrip('\n')))
    return retl

def checklevel(l):
    if isinstance(l[0],list) and isinstance(l[1],list):
        return 2,True
    if isinstance(l[0],list):
        return l[0],True
    if isinstance(l[1],list):
        return l[1],True
    else:
        return None,False

def countlevels(l):
    count=0
    ch=True
    while(ch):
        count+=1
        li=l
        l,ch=checklevel(l)
        if l==2:
            c1=countlevels(li[0])
            c2=countlevels(li[1])
            count+=max(c1,c2)
            ch=False
    return count                

def add(lisA,lisB):
    lisC=[lisA,lisB]
    return lisC

def explodex(l,level):
    for i in range(level-5):
        li=l
        l,ch=checklevel(l)
        if l==2:
            c1=countlevels(li[0])
            if c1==level-i-1:
                l=li[0]
            else:
                c2=countlevels(li[1])
                if c2==level-1-i:
                    l=li[1]        
    return l

input=readfile('Day18_sample_input.txt')
l=input[0]
for i in range(1,len(input)):
    l=add(l,input[i])
    lvl=countlevels(l)
    if lvl>4:
        for i in range(lvl,4,-1):
            l=explodex(l,i)
            l=Day18_2021.explode(l)
print(l)           