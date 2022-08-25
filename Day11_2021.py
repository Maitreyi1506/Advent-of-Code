
def readinput(x):
    f=open(x,'r')
    l=f.readlines()
    lis=[]
    for line in l:
        row=[]
        for character in line:
            if line[-1]!=character: 
                row.append(int(character))
        lis.append(row)
    return lis

def inc():
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=1

def flash(lis):
    for pt in lis:
        for k in range(pt[0]-1,pt[0]+2):
            for l in range(pt[1]-1,pt[1]+2):
                if k>=0 and k<len(board) and l>=0 and l<len(board[0]):
                    board[k][l]+=1

def check(flashed):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>9:
                if [i,j] not in flashed:
                    return True
    return False

def func(flashed):
    pts=[]
    for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]>9:
                    if [i,j] not in flashed:
                        pts.append([i,j])
    flash(pts)
    return pts

def step():
    flashed=[]
    count=0
    inc()
    list1=[]
    list1=func(flashed)
    flashed.extend(list1)
    while(check(flashed)):
        list1=[]
        list1=func(flashed)
        flashed.extend(list1)        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>9:    
                board[i][j]=0
                count+=1
    return count



def main():
    count=0
    stepcount=0
    while(stepcount!=100):
        stepcount=step()
        count+=1
        
        
        #print('step ',m+1,' done')
        #print(count)
        #for row in board:
        #   print(row)
    return count


board=readinput('Day11_2021_input.txt')
#print(input)
print(main())
#for row in board:
#    print(row)
print('endcode')