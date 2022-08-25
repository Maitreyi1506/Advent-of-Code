
def readfile(x):
    f=open(x,'r')
    l=f.readlines()
    retl=[]
    x,y=0,0
    for i in l:
        retl.append(eval(i.rstrip('\n')))
    return retl

def add(lisA,lisB):
    lisC=[lisA,lisB]
    return lisC

def first(A,x):
    if isinstance(A,list):
        if isinstance (A[0],list):
            if isinstance(A[0][0],list):
                if isinstance(A[0][0][0],list):
                    if isinstance(A[0][0][0][0],list):
                        return [[[[[A[0][0][0][0][0]+x,A[0][0][0][0][1]],A[0][0][0][1]],A[0][0][1]],A[0][1]],A[1]]
                    else:
                        return [[[[A[0][0][0][0]+x,A[0][0][0][1]],A[0][0][1]],A[0][1]],A[1]]
                else:
                    return [[[A[0][0][0]+x,A[0][0][1]],A[0][1]],A[1]]
            else:
                return [[A[0][0]+x,A[0][1]],A[1]]
        else:
            return [A[0]+x,A[1]]
    else:
        return A+x

def last(A,x):
    if isinstance(A,list):
        if isinstance (A[1],list):
            if isinstance(A[1][1],list):
                if isinstance(A[1][1][1],list):
                    if isinstance(A[1][1][1][1],list):
                        return [A[0],[A[1][0],[A[1][1][0],[A[1][1][1][0],[A[1][1][1][1][0],A[1][1][1][1][1]+x]]]]]
                    else:
                        return [A[0],[A[1][0],[A[1][1][0],[A[1][1][1][0],A[1][1][1][1]+x]]]]
                else:
                    return [A[0],[A[1][0],[A[1][1][0],A[1][1][1]+x]]]
            else:
                return [A[0],[A[1][0],A[1][1]+x]]
        else:
            return [A[0],A[1]+x]
    else:
        return A+x

#[[[2,[[9,8],1]],3],4]
#[[[2,[0,9]],3],4]         
#x1=[[2,[1,[9,8]]],3]
#x2=[2,[1,[9,8]]]
#x3=2
#x4=1
#y4=[9.8]
#y3=[1,[9,8]]
#y2=3        
#y1=4
def explode(list1):
    x1,y1=list1[0],list1[1]
    if isinstance(x1,list):
        x2,y2=x1[0],x1[1]
        if isinstance(x2,list):
            x3,y3=x2[0],x2[1]
            if isinstance(x3,list):
                x4,y4=x3[0],x3[1]
                if isinstance(x4,list):                 #[[[[[x4[0],x4[1]],y4],y3],y2],y1] ==> [[[[0,x4[1]+y4],y3],y2],y1]
                    return [[[[0,first(y4,x4[1])],y3],y2],y1]
                elif isinstance(y4,list):               #[[[[x4,[y4[0]+y4[1]]],y3],y2],y1] ==> [[[[x4+y4[0],0],y3+y4[1]],y2],y1]
                    return [[[[last(x4,y4[0]),0],first(y3,y4[1])],y2],y1]
                else:
                    pass
            if isinstance(y3,list):
                x4,y4=y3[0],y3[1]
                if isinstance(x4,list):                 #[[[x3,[[x4[0],x4[1]],y4]],y2],y1] ==>[[[x3+x4[0],[0,x4[1]+y4]],y2],y1]
                    return [[[last(x3,x4[0]),[0,first(y4,x4[1])]],y2],y1]    
                elif isinstance(y4,list):               #[[[x3,[x4,[y4[0],y4[1]]]],y2],y1] ==> [[[x3,[x4+y4[0],0]],y2+y4[1]],y1]
                    return [[[x3,[last(x4,y4[0]),0]],first(y2,y4[1])],y1]   
                else:
                    pass
            else:
                pass
        if isinstance(y2,list):
            x3,y3=y2[0],y2[1]
            if isinstance(x3,list):
                x4,y4=x3[0],x3[1]
                if isinstance(x4,list):             #[[x2,[[[x4[0],x4[1]],y4],y3]],y1] ==> [[x2+x4[0],[[0,x4[1]+y4],y3]],y1]
                    return [[last(x2,x4[0]),[[0,first(y4,x4[1])],y3]],y1]
                elif isinstance(y4,list):           #[[x2,[[x4,[y4[0],y4[1]]],y3]],y1] ==> [[x2,[[x4+y4[0],0],y3+y4[1]]],y1]
                    return [[x2,[[last(x4,y4[0]),0],first(y3,y4[1])]],y1]      
                else:
                    pass
            if isinstance(y3,list):
                x4,y4=y3[0],y3[1]
                if isinstance(x4,list):             #[[x2,[x3,[[x4[0],x4[1]],y4]]],y1] ==> [[x2,[x3+x4[0],[0,x4[1]+y4]]],y1]
                    return [[x2,[last(x3,x4[0]),[0,first(y4,x4[1])]]],y1]
                elif isinstance(y4,list):           #[[x2,[x3,[x4,[y4[0],y4[1]]]]],y1] ==> [[x2,[x3,[x4+y4[0],0]]],y1+y4[1]]
                    return [[x2,[x3,[last(x4,y4[0]),0]]],first(y1,y4[1])]
                else:
                    pass
            else:
                pass
        else:
            pass
    if isinstance(y1,list):
        x2,y2=y1[0],y1[1]
        if isinstance(x2,list):
            x3,y3=x2[0],x2[1]
            if isinstance(x3,list):
                x4,y4=x3[0],x3[1]
                if isinstance(x4,list):            #[x1,[[[[x4[0],x4[1]],y4],y3],y2]] ==> [x1+x4[0],[[[0,x4[1]+y4],y3],y2]]
                    return [last(x1,x4[0]),[[[0,first(y4,x4[1])],y3],y2]]
                elif isinstance(y4,list):          #[x1,[[[x4,[y4[0],y4[1]]],y3],y2]] ==> [x1,[[[x4+y4[0],0],y3+y4[1]],y2]]
                    return [x1,[[[last(x4,y4[0]),0],first(y3,y4[1])],y2]]
                else:
                    pass
            if isinstance(y3,list):
                x4,y4=y3[0],y3[1]
                if isinstance(x4,list):             #[x1,[[x3,[[x4[0],x4[1]],y4]],y2]] ==> [x1,[[x3+x4[0],[0,x4[1]+y4]],y2]]
                    return [x1,[[last(x3,x4[0]),[0,first(y4,x4[1])]],y2]]
                elif isinstance(y4,list):           #[x1,[[x3,[x4,[y4[0],y4[1]]]],y2]] ==> [x1,[[x3,[x4+y4[0],0]],y2+y4[1]]]
                    return [x1,[[x3,[last(x4,y4[0]),0]],first(y2,y4[1])]]
                else:
                    pass
            else:
                pass
        if isinstance(y2,list):
            x3,y3=y2[0],y2[1]
            if isinstance(x3,list):
                x4,y4=x3[0],x3[1]
                if isinstance(x4,list):             #[x1,[x2,[[[x4[0],x4[1]],y4],y3]]] ==> [x1,[x2+x4[0],[[0,x4[1]+y4],y3]]]
                    return [x1,[last(x2,x4[0]),[[0,first(y4,x4[1])],y3]]]
                elif isinstance(y4,list):           #[x1,[x2,[[x4,[y4[0],y4[1]]],y3]]] ==> [x1,[x2,[[x4+y4[0],0],y3+y4[1]]]]
                    return [x1,[x2,[[last(x4,y4[0]),0],first(y3,y4[1])]]]
                else:
                    pass
            if isinstance(y3,list):
                x4,y4=y3[0],y3[1]
                if isinstance(x4,list):             #[x1,[x2,[x3,[[x4[0],x4[1]],y4]]]] ==> [x1,[x2,[x3+x4[0],[0,x4[1]+y4]]]]
                    return [x1,[x2,[last(x3,x4[0]),[0,first(y4,x4[1])]]]]
                elif isinstance(y4,list):           #[x1,[x2,[x3,[x4,[y4[0],y4[1]]]]]] ==> [x1,[x2,[x3,[x4+y4[0],0]]]]
                    return [x1,[x2,[x3,[last(x4,y4[0]),0]]]]
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def split(lis):
    x1,y1=lis[0],lis[1]
    if isinstance(x1,int):
        if x1>9:
            x1=[int(x1/2),x1-int(x1/2)]
            return [x1,y1]
        else:
            pass
    else:
        x2,y2=x1[0],x1[1]
        if isinstance(x2,int):
            if x2>9:
                x2=[int(x2/2),x2-int(x2/2)]
                return [[x2,y2],y1]
            else:
                pass
        else:
            x3,y3=x2[0],x2[1]
            if isinstance(x3,int):
                if x3>9:
                    x3=[int(x3/2),x3-int(x3/2)]
                    return [[[x3,y3],y2],y1]
                else:
                    pass
            else:
                x4,y4=x3[0],x3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [[[[x4,y4],y3],y2],y1]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [[[[x4,y4],y3],y2],y1]
                    else:
                        pass
                else:
                    pass
            if isinstance(y3,int):
                if y3>9:
                    y3=[int(y3/2),y3-int(y3/2)]
                    return [[[x3,y3],y2],y1]
                else:
                    pass
            else:
                x4,y4=y3[0],y3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [[[x3,[x4,y4]],y2],y1]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [[[x3,[x4,y4]],y2],y1]
                    else:
                        pass
                else:
                    pass
        if isinstance(y2,int):
            if y2>9:
                y2=[int(y2/2),y2-int(y2/2)]
                return [[x2,y2],y1]
            else:
                pass
        else:
            x3,y3=y2[0],y2[1]
            if isinstance(x3,int):
                if x3>9:
                    x3=[int(x3/2),x3-int(x3/2)]
                    return [[x2,[x3,y3]],y1]
                else:
                    pass
            else:
                x4,y4=x3[0],x3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [[x2,[[x4,y4],y3]],y1]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [[x2,[[x4,y4],y3]],y1]
                    else:
                        pass
                else:
                    pass
            if isinstance(y3,int):
                if y3>9:
                    y3=[int(y3/2),y3-int(y3/2)]
                    return [[x2,[x3,y3]],y1]
                else:
                    pass
            else:
                x4,y4=y3[0],y3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [[x2,[x3,[x4,y4]]],y1]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [[x2,[x3,[x4,y4]]],y1]
                    else:
                        pass
                else:
                    pass
    if isinstance(y1,int):
        if y1>9:
            y1=[int(y1/2),y1-int(y1/2)]
            return [x1,y1]
    else:
        x2,y2=y1[0],y1[1]
        if isinstance(x2,int):
            if x2>9:
                x2=[int(x2/2),x2-int(x2/2)]
                return [x1,[x2,y2]]
            else:
                pass
        else:
            x3,y3=x2[0],x2[1]
            if isinstance(x3,int):
                if x3>9:
                    x3=[int(x3/2),x3-int(x3/2)]
                    return [x1,[[x3,y3],y2]]
                else:
                    pass
            else:
                x4,y4=x3[0],x3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [x1,[[[x4,y4],y3],y2]]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [x1,[[[x4,y4],y3],y2]]
                    else:
                        pass
                else:
                    pass
            if isinstance(y3,int):
                if y3>9:
                    y3=[int(y3/2),y3-int(y3/2)]
                    return [x1,[[x3,y3],y2]]
                else:
                    pass
            else:
                x4,y4=y3[0],y3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [x1,[x3,[x4,y4]],y2]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [x1,[[x3,[x4,y4]],y2]]
                    else:
                        pass
                else:
                    pass        
        if isinstance(y2,int):
            if y2>9:
                y2=[int(y2/2),y2-int(y2/2)]
                return [x1,[x2,y2]]
            else:
                return lis
        else:
            x3,y3=y2[0],y2[1]
            if isinstance(x3,int):
                if x3>9:
                    x3=[int(x3/2),x3-int(x3/2)]
                    return [x1,[x2,[x3,y3]]]
                else:
                    pass
            else:
                x4,y4=x3[0],x3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [x1,[x2,[[x4,y4],y3]]]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [x1,[x2,[[x4,y4],y3]]]
                    else:
                        pass
                else:
                    pass
            if isinstance(y3,int):
                if y3>9:
                    y3=[int(y3/2),y3-int(y3/2)]
                    return [x1,[x2,[x3,y3]]]
                else:
                    return lis
            else:
                x4,y4=y3[0],y3[1]
                if isinstance(x4,int):
                    if x4>9:
                        x4=[int(x4/2),x4-int(x4/2)]
                        return [x1,[x2,[x3,[x4,y4]]]]
                    else:
                        pass
                if isinstance(y4,int):
                    if y4>9:
                        y4=[int(y4/2),y4-int(y4/2)]
                        return [x1,[x2,[x3,[x4,y4]]]]
                    else:
                        return lis
                else:
                    return lis

def exploop(l):
    original=l
    li=l
    while(l):
        l=explode(l)
        if (l):
            li=l
    if li==original:
        return li,False
    else:
        return li,True


#l=[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]


input=readfile('Day18_sample_input.txt')
#print(input)
l=add(input[0],input[1])
ch=True
while(ch):
    l,ch = exploop(l)
    l=split(l)
#print(l)
for i in range(2,len(input)):
    l=add(l,input[i])
    ch=True
    while(ch):
        l,ch = exploop(l)
        l=split(l)
#print(l)