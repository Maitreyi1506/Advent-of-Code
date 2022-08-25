
def readfile(x):
    f=open(x,'r')
    lines=f.readlines()
    board=[]
    for line in lines:
        row=[]
        for character in line:
            if character!='\n':
                row.append(character)
        board.append(row)
    return board

def step(oldboard,stepno):
    newboard=oldboard
    flag,flag2,flag3=False,None,True
    for i in range(len(newboard)):
        for j in range(len(newboard[i])):
            if j==len(newboard[i])-1:
                if newboard[i][j]=='>' and newboard[i][0]=='.' and flag2!=j and flag3:
                    newboard[i][j],newboard[i][0],flag='.','>',True
            else:
                if newboard[i][j]=='>' and newboard[i][j+1]=='.' and flag2!=j:
                    if j==0:
                        flag3=False
                    newboard[i][j],newboard[i][j+1],flag,flag2='.','>',True,j+1
        flag2,flag3=None,True
    for i in range(len(newboard[0])):
        for j in range(len(newboard)):
            if j==len(newboard)-1:
                if newboard[j][i]=='v' and newboard[0][i]=='.' and flag2!=j and flag3:
                    newboard[j][i],newboard[0][i],flag='.','v',True
            else:
                if newboard[j][i]=='v' and newboard[j+1][i]=='.' and flag2!=j:
                    if j==0:
                        flag3=False
                    newboard[j][i],newboard[j+1][i],flag,flag2='.','v',True,j+1 
        flag2,flag3=None,True
    if flag:
        stepno+=1
    return flag,newboard,stepno

input=readfile('Day25_2021_input.txt')
flag=True
count=0
board=input
while flag:
    flag,board,count=step(board,count)
    #print(count)
    #for row in board:
    #    print(row)
print(count+1)    
#for row in board:
#    print(row)   
                
