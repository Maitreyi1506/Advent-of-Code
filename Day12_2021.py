allpaths=[]
def reading(x):
    f=open(x,'r')
    l1=f.readlines()
    l3=[]
    for l in l1:
        l2=[]
        x,y=l.split('-')
        l2=[x,y.rstrip('\n')]
        l3.append(l2)
    return l3


def findpath(paths,ele,route):
    currentroute=[] 
    for path in paths:
        if ele in path:
            currentroute=route.copy()
            idx=1-path.index(ele)
            ele2=path[idx]
            if ele2.islower():
                if ele2 not in currentroute:
                    currentroute.append(ele2)
                    if ele2=='end':
                        allpaths.append(currentroute)
                    else:
                        findpath(paths,ele2,currentroute)
            elif ele2.isupper():
                currentroute.append(ele2)
                findpath(paths,ele2,currentroute)
            else:
                pass
        else:
            pass

input=reading('Day12_2021_input.txt')
#for lis in input:

findpath(input,'start',['start'])
print(len(allpaths))