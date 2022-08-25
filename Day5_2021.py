board=[]
for j in range(1000):
    row=[]
    for i in range(1000):
        row.append(0)
    board.append(row)

def readfile(x):
    f=open(x,'r')
    list=f.readlines()
    list2=[]
    for entry in list:
        list3=[]
        init,final=entry.split('->')
        x1,y1=init.split(',')
        x2,y2=final.split(',')
        list3=[int(x1),int(y1),int(x2),int(y2)]
        list2.append(list3)
    return list2

l=['0,9 -> 5,9','8,0 -> 0,8','9,4 -> 3,4','2,2 -> 2,1','7,0 -> 7,4','6,4 -> 2,0','0,9 -> 2,9','3,4 -> 1,4','0,0 -> 8,8','5,5 -> 8,2']
list=readfile('Day5_2021_input.txt')
#list=readfile(l)
for set in list:
    if set[0]==set[2]:
        if set[1]<set[3]:
            for index in range(set[1],set[3]+1):
                board[index][set[0]]+=1
        else:
            for index in range(set[3],set[1]+1):
                board[index][set[0]]+=1
    elif set[1]==set[3]:
        if set[0]<set[2]:
            for index in range(set[0],set[2]+1):
                board[set[1]][index]+=1
        else:
            for index in range(set[2],set[0]+1):
                board[set[1]][index]+=1
    else:
        if set[2]>set[0] and set[3]>set[1]:
            for index1,index2 in zip(range(set[0],set[2]+1,1),range(set[1],set[3]+1,1)):
                board[index2][index1]+=1
        elif set[2]<set[0] and set[3]>set[1]:
            for index1,index2 in zip(range(set[0],set[2]-1,-1),range(set[1],set[3]+1,1)):
                board[index2][index1]+=1
        elif set[2]>set[0] and set[3]<set[1]:
            for index1,index2 in zip(range(set[0],set[2]+1,1),range(set[1],set[3]-1,-1)):
                board[index2][index1]+=1
        else:
            for index1,index2 in zip(range(set[0],set[2]-1,-1),range(set[1],set[3]-1,-1)):
                board[index2][index1]+=1

count=0
for row in board:
    #print(row)
    for number in row:
        if number>1:
            count+=1
print(count)