from statistics import mode
def readfile(x):
    f=open(x,'r')
    list=f.readlines()
    return list

def convert(x):
    if x==1:
        x=0
    elif x==0:
        x=1
    else:
        pass
    return x

def process(inputlist):
    list,gammalist,epsilonlist=[],[],[]
    gamma,epsilon=0,0
    for i in range(len(inputlist[0])-1):
        for number in inputlist:
            list.append(int(number[i]))
        m=mode(list)
        gammalist.append(m)
        epsilonlist.append(convert(m))
        list=[]
    for i in range(len(gammalist)):
        gamma+=gammalist[i]*2**(len(gammalist)-1-i)
    for j in range(len(epsilonlist)):
        epsilon+=epsilonlist[j]*2**(len(epsilonlist)-1-j)
    return gamma,epsilon

def processoxygen(inputlist):
    inplist,list=[],[]
    for i in range(len(inputlist[0])-1):
        for number in inputlist:
            list.append(int(number[i]))
        m=mode(list)
        if m==0:
            k=list.count(1)
            l=list.count(0)
            if k==l:
                m=1
        list=[]
        for number in inputlist:
            if int(number[i])==m:
                inplist.append(number)
        inputlist=inplist.copy()
        inplist=[]
    return inputlist

def processco2(inputlist):
    inplist,list=[],[]
    for i in range(len(inputlist[0])-1):
        for number in inputlist:
            list.append(int(number[i]))
        m=mode(list)
        if m==0:
            k=list.count(1)
            l=list.count(0)
            if k==l:
                m=1
        list=[]
        n=convert(m)
        if(len(inputlist)>1):
            for number in inputlist:
                if int(number[i])==n:
                    inplist.append(number)
            inputlist=inplist.copy()
            inplist=[]
    return inputlist

def binarytodecimal(singleunitlist):
    n=len(singleunitlist[0])-1
    k=singleunitlist[0]
    decimal=0
    for i in range(n):
        decimal+=int(k[i])*2**(n-1-i)        
    return decimal

#def processinput(inputlist):
    list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12=[],[],[],[],[],[],[],[],[],[],[],[]
    for number in inputlist:
        list1.append(int(number[0]))
        list2.append(int(number[1]))
        list3.append(int(number[2]))
        list4.append(int(number[3]))
        list5.append(int(number[4]))
        list6.append(int(number[5]))
        list7.append(int(number[6]))
        list8.append(int(number[7]))
        list9.append(int(number[8]))
        list10.append(int(number[9]))
        list11.append(int(number[10]))
        list12.append(int(number[11]))
    a,b,c,d,e,f,g,h,i,j,k,l=mode(list1),mode(list2),mode(list3),mode(list4),mode(list5),mode(list6),mode(list7),mode(list8),mode(list9),mode(list10),mode(list11),mode(list12)
    gamma=a*2048+b*1024+c*512+d*256+e*128+f*64+g*32+h*16+i*8+j*4+k*2+l
    a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1=convert(a),convert(b),convert(c),convert(d),convert(e),convert(f),convert(g),convert(h),convert(i),convert(j),convert(k),convert(l)
    epsilon=a1*2048+b1*1024+c1*512+d1*256+e1*128+f1*64+g1*32+h1*16+i1*8+j1*4+k1*2+l1
    return gamma,epsilon

sample=['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
myinput=readfile('Day3_2021_input.txt')
#g,e=process(myinput)
#print(g*e)
list3,list4=processoxygen(myinput),processco2(myinput)
a,b=binarytodecimal(list3),binarytodecimal(list4)
print(a*b)