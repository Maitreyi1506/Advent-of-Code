a=[1721,979,366,299,675,1456]

def prod(list):
    for i in list:
        for j in list:
            for k in list:
                if i+j+k==2020:
                    return i*j*k
                else:
                    pass

def readinput(x):
    f=open(x,'r')
    arr=f.readlines()
    arr2=[]
    for i in arr:
        arr2.append(int(i))
    return arr2

myinput=readinput('Day1_2020_input.txt')
print(prod(myinput))