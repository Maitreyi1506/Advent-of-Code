#row1=[22,13,17,11,0]
#row1=['X',13,17,11,0]
#row2=[8,2,23,4,24]
#row2=['X',2,23,4,24]
#row3=[21,9,14,16,7]
#row3=['X',9,14,16,7]
#row4=[6,10,3,18,5]
#row4=['X',10,3,18,5]
#row5=[1,12,20,15,19]
#row5=['X',12,20,15,19]
#board=[row1,row2,row3,row4,row5]
    
#list=[7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

def readfile(x):
    list,boards=[],[]
    f=open(x,'r')
    contents=f.readlines()
    list=contents[0].split(',')
    for i in range(len(list)):
        list[i]=int(list[i])
    for i in range(1,len(contents),6):
        board=[]
        for j in range(1,6):
            row=contents[i+j].split()
            for k in range(len(row)):
                row[k]=int(row[k])
            board.append(row)
        boards.append(board)
    return list,boards
        
l,b=readfile('Day4_2021_input.txt')
#print(l,b)
#readfile('Day4_sample_input.txt')
def check(board):
    count=0
    for row in board:
        for nm in row:
            if nm=='X':
               count+=1
        if count==5:
           return True
        count=0
    count=0
    for idx in range(len(board[0])):
        for row in board:
            if row[idx]=='X':
                count+=1
        if count==5:
            return True
        count=0
    return False

def value(board):
    sum=0
    for row in board:
        for number in row:
            if number!='X':
                sum+=number
    return sum

def find(board,x):
    a=0
    for row in board:
        for number in row:
            if number==x:
                a=number
                row[(row.index(number))]='X'
    if check(board)==True:
        return board,a*value(board)
    else:
        return None,None
Ans=None

for number in l:
    todelete=[]
    for board in b:
        currentboard,currentvalue=find(board,number)
        if currentvalue!=None:
            if (len(b)!=1):
                todelete.insert(0,b.index(board))
                print(len(b))
            else:
                print(currentvalue)
                break
    else:
        if len(todelete):
            for idx in todelete:
                del b[idx]
        continue
    break

print("endcode")