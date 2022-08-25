
def readfile(x):
    f=open(x,'r')
    list=[]
    for line in f:
        for character in line:
            list.append(character)
    return list

input=readfile('Day1_2015_input.txt')

upfloor=input.count('(')
downfloor=input.count(')')
diff=upfloor-downfloor
print(upfloor,downfloor,diff)

score=0
count=0
for floor in input:
    count+=1
    if floor=='(':
        score+=1
    elif floor==')':
        score-=1
    if score==-1:
        print(count)
        break