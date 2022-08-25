
def readfile(x):
    f=open(x,'r')
    lis=f.readlines()
    points=[]
    for l in lis:
        if l=='\n':
            idx=lis.index(l)
            break
        else:
            x,y=l.split(',')
            pt=[int(x),int(y)]
            points.append(pt)
    folds=[]
    for i in range(idx+1,len(lis)):
        str,str2,str3=lis[i].split(' ')
        foldletter,foldnumber=str3.split('=')
        fold=[foldletter,int(foldnumber)]
        folds.append(fold)
    return points,folds

def createboard():
    brd=[]
    for i in range(1500):
        row=[]
        for i in range(1500):
            row.append(0)
        brd.append(row)
    return brd

def plotpts(pts,plotboard):
    for pt in pts:
        plotboard[pt[1]][pt[0]]='X'
    return plotboard

def fold(conditions,board):
    for fold in conditions:
        if fold[0]=='x':
            for i in range(fold[1]+1,len(board[0])):
                for x in range(len(board)):
                    if board[x][i]=='X':
                        board[x][2*fold[1]-i]='X'
                        board[x][i]=0
        elif fold[0]=='y':
            for i in range(fold[1]+1,len(board)):
                for x in range(len(board[i])):
                    if board[i][x]=='X':
                        board[2*fold[1]-i][x]='X'
                        board[i][x]=0
        else:
            pass
    return board

def count(finalboard):
    count=0
    for row in finalboard:
        for sym in row:
            if sym=='X':
                count+=1
    return count

def printlist(board):
    for row in board:
        for column in row:
            if column==0:
                print('.',end='')
            else:
                print(column,end='')
        print('\n')

A,B=readfile('Day13_2021_input.txt')
output=plotpts(A,createboard())
#for row in output:
#    print(row)
output2=fold(B,output)
printlist(output2)
output3=count(output2)
print(output3)

