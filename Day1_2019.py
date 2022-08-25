

def readfile(x):
    f=open(x,'r')
    inp=f.readlines()
    reinp=[]
    for no in inp:
        reinp.append(int(no))
    return reinp

def process(lis):
    #fuel=[]
    sum=0
    y=1
    count=0
    for x in lis:
        y=x
        while y!=0:
            y=int(y/3)-2
            if y<0:
                break
            #print(y)
            #fuel.append(y)
            sum+=y
        count+=1
        print('Step ',count,' completed.')
    return sum

input=readfile('Day1_2019_input.txt')
print(len(input))
#ans=0
#rans=inf
#while rans!=0:
#    rans,input=process(input)
#    ans+=rans
ans=process(input)
print(ans)
print('endcode')