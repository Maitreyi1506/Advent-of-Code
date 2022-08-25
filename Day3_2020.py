board=[]

def readboard(x):
    f=open(x,'r')
    lines=f.readlines()
    for line in lines:
        board.append(line)
    return board

newboard=readboard('Day3_2020_input.txt')

print(len(newboard))
m=0
flag=0

for line in board:
    li=[]
    li[:0]=line
    if li[m]=='#':
        flag+=1
    m+=3
    if m>=len(li):
        m=m-len(li)
print(flag)

