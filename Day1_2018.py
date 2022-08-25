def readfile(x):
    arr=[]
    f=open(x,'r')
    lines=f.readlines()
    for line in lines:
        l=int(line)
        arr.append(l)
    return arr
    
myinput=readfile('Day1_input.txt')
#print(sum(myinput))

def duplicate(arr):
    freq=[]
    sum=0
    flag=0
    while(flag==0):
        for a in arr:
            sum+=a
            if sum in freq:
                flag+=1
                return sum
            else:
                freq.append(sum)
    
sample=[3,3,4,-2,-4]
output=duplicate(myinput)
print(output)