
from numpy import sqrt

pos=[10,10]
dir='N'
board=[]
for i in range(21):
    row=[]
    for j in range(21):
        row.append('.')
    board.append(row)
board[10][10]='X'

def readfile(x):
    f=open(x,'r')
    inp=f.readlines()
    lis=inp[0].split(' ')
    return lis

def direction(change,mag,oldpos):
    if dir=='N' and change=='L':
        newdir='W'
        newpos=[oldpos[0],oldpos[1]-mag]
    elif dir=='N' and change=='R':
        newdir='E'
        newpos=[oldpos[0],oldpos[1]+mag]
    elif dir=='E' and change=='L':
        newdir='N'
        newpos=[oldpos[0]+mag, oldpos[1]]
    elif dir=='E' and change=='R':
        newdir='S'
        newpos=[oldpos[0]-mag,oldpos[1]]
    elif dir=='S' and change=='L':
        newdir='E'
        newpos=[oldpos[0],oldpos[1]+mag]
    elif dir=='S' and change=='R':
        newdir='W'
        newpos=[oldpos[0],oldpos[1]-mag]
    elif dir=='W' and change=='L':
        newdir='S'
        newpos=[oldpos[0]-mag,oldpos[1]]
    elif dir=='W' and change=='R':
        newdir='N'
        newpos=[oldpos[0]+mag,oldpos[1]]
    else:
        pass
    return newdir,newpos

def movement(oldpos,newpos):
    if oldpos[0]==newpos[0]:
        for i in range(min(oldpos[1],newpos[1]),max(oldpos[1],newpos[1])):
            if board[oldpos[0]][i]=='X':
                return [newpos[0],i]
            else:
                board[oldpos[0]][i]='X'
    elif oldpos[1]==newpos[1]:

            
# time is up, change board from 10X10 to 100X100; 

input=readfile('Day1_sample_input.txt')
#print(input)
print(len(input))
visitedpos=[pos]
for idx in range(len(input)):
    step=input[idx]
    if idx==len(input)-1:
        dir,pos=direction(step[0],int(step[1:]),pos)
    else:
        dir,pos=direction(step[0],int(step[1:-1]),pos)
    if pos in visitedpos:
        break
    else:
        visitedpos.append(pos)
print(pos)
value=abs(pos[0])+abs(pos[1])
print(value)
print(visitedpos)
#value2=sqrt(pow(pos[0],2)+pow(pos[1],2))
#print(value2)