#1 @ 871,327: 16x20

def readfile(xfile):
    fh=open(xfile,'r')
    claimlist=[]
    lines=fh.readlines()
    for line in lines:
        id,temp,offset,dim= line.split()
        offx,offy=offset.replace(':','').split(',')
        l,b=dim.split('x')
        claim=[id,int(offx),int(offy),int(l),int(b)]
        claimlist.append(claim)
    return claimlist

def initboard(dimx,board=[]):
    a=[]
    for i in range(dimx):
        b=[]
        for j in range(dimx):
            if len(board)>0:
                b.append(board[i][j])
            else:
                b.append(0)
        a.append(b)
    return a


def markboard(claim,board):
    newboard=initboard(len(board),board)
    for i in range(claim[3]):
        for j in range(claim[4]):
            newboard[claim[1]+i][claim[2]+j]+=1
    return newboard

def countduplicate(board):
    count=0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]>1:
                count+=1
    return count

def findoverlap(board,claim):
    area=claim[3]*claim[4]
    sum=0
    for i in range(claim[3]):
        for j in range(claim[4]):
            sum+=board[claim[1]+i][claim[2]+j]
    return sum==area
claimlist= readfile('2018_3_1input.txt')

#print(claimlist[2])
brick=initboard(1200)
for i in range(len(claimlist)):
   print(f'claim number {i} out of {len(claimlist)}')
   brick=markboard(claimlist[i],brick)
for i in range(len(claimlist)):
    if findoverlap(brick,claimlist[i]):
        print(f'claim {claimlist[i]} does not have an overlap')

#newbrick=markboard(claimlist[2],newbrick)
#print(countduplicate(brick))
#print(newbrick[246][819])


