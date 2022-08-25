from collections import Counter
def read(x):
    f=open(x,'r')
    lis=f.readlines()
    str=lis[0]
    A=[]
    A[:0]=str
    del A[-1]
    dict={}
    for idx in range(2,len(lis)):
        pair,insertion=lis[idx].split(' ->')
        B=[]
        B[:0]=insertion
        dict[pair]=B[1]
    return A,dict

def iteration(poly,rules):
    temp=[]
    for idx in range(len(poly)-1):
        tuple=(poly[idx],poly[idx+1])
        str=''.join(tuple)
        temp.append(poly[idx])
        temp.append(rules[str])
    temp.append(poly[-1])
    return temp

def alt(exp,rules):
    dict2={}
    for idx in range(len(exp)-1):
        tuple=(exp[idx],exp[idx+1])
        str=''.join(tuple)
        if str in dict2.keys():
            dict2[str]+=1
        else:
            dict2[str]=1
    return dict2

def altiteration(rules,dict):
    lis=list(dict.keys())
    dicttoadd={}
    for pair in lis:
        ch=rules[pair]
        ch1,ch2=pair[0],pair[1]
        tuple1,tuple2=(ch1,ch),(ch,ch2)
        pair1=''.join(tuple1)
        pair2=''.join(tuple2)
        if pair1 in dicttoadd.keys():
            dicttoadd[pair1]+=dict[pair]
        else:
            dicttoadd[pair1]=dict[pair]
        if pair2 in dicttoadd.keys():
            dicttoadd[pair2]+=dict[pair]
        else:
            dicttoadd[pair2]=dict[pair]
    return dicttoadd

def final(pairs):
    dict={}
    A=list(pairs.keys())
    B=list(pairs.values())
    for pair in A:
        ch1,ch2=pair[0],pair[1]
        if ch1 in dict:
            dict[ch1]+=B[A.index(pair)]
        else:
            dict[ch1]=B[A.index(pair)]
        if ch2 in dict:
            dict[ch2]+=B[A.index(pair)]
        else:
            dict[ch2]=B[A.index(pair)]
    C=list(dict.keys())
    D=list(dict.values())
    for value in D:
        if value%2==0:
            dict[C[D.index(value)]]=value/2
        else:
            dict[C[D.index(value)]]=(value+1)/2
    return dict

polynomial,instr=read('Day14_2021_input.txt')
'''print(alt(polynomial,instr))
A,B,C,D=[],[],[],[]
A[:0]='NCNBCHB'
print(alt(A,instr))
B[:0]='NBCCNBBBCBHCB'
print(alt(B,instr))
C[:0]='NBBBCNCCNBBNBNBBCHBHHBCHB'
print(alt(C,instr))
D[:0]='NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
print(alt(D,instr))'''
mydict=alt(polynomial,instr)
for i in range(40):
    #temppoly=iteration(polynomial,instr)
    #polynomial=temppoly.copy()
    mydict=altiteration(instr,mydict)
    print('Step ',i+1,' done')
mydict2=final(mydict)
#dict=Counter(polynomial)
print(max(list(mydict2.values()))-min(list(mydict2.values())))
