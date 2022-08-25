def read(x):
    f=open(x,'r')
    lis=f.readlines()
    list=[]
    for str in lis:
        lis1=[]
        lis1[:0]=str
        list.append(str)
    return list

def openblock(arr):
    for sym in arr:
        if sym=='(' or sym=='[' or sym=='{' or sym=='<':
            