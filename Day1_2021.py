
def readfile(x):
    f=open(x,'r')
    list1=f.readlines()
    list=[]
    for i in list1:
        list.append(int(i))
    return list

def incval(input):
    count=0
    for x in range(1,len(input)):
        if input[x]>input[x-1]:
            count+=1
    return count

def part2(input):
    slidinglist=[]
    value=0
    for x in range(len(input)):
        if x+3<=len(input):
            for i in range(3):
                value+=input[x+i]
            slidinglist.append(value)
            x+=i
        value=0
    return slidinglist

sample=[199,200,208,210,200,207,240,269,260,263]
input=readfile('Code1_input.txt')
print(len(input))

