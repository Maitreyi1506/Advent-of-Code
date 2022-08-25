def readfile(x):
    file=open(x,'r')
    list=file.readlines()
    return list

def convert(list1):
    direction=[]
    magnitude=[]
    for instruction in list1:
        dir,mag=instruction.split()
        direction.append(dir)
        magnitude.append(int(mag))
    return direction,magnitude

def values(lista,listb):
    horizontal,depth=0,0
    for idx in range(len(lista)):
        if lista[idx]=='forward':
            horizontal+=listb[idx]
        elif lista[idx]=='up':
            depth-=listb[idx]
        elif lista[idx]=='down':
            depth+=listb[idx]
        else:
            pass
    return horizontal,depth

sample=['forward 5','down 5','forward 8','up 3','down 8','forward 2']
myinput=readfile('Day1_2021_input.txt')
A,B=convert(myinput)
finalhori,finaldeep=values(A,B)
print(finalhori*finaldeep)


