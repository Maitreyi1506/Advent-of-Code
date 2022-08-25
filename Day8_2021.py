
def readfile(x):
    f=open(x,'r')
    list=f.readlines()
    output=[]
    output2=[]
    for li in list:
        useless,useful=li.split('|')
        output.append(useful)
        output2.append(useless)
    return output,output2

def process(list):
    count=0
    for li in list:
        n1,n2,n3,n4=li.split()
        for n in n1,n2,n3,n4:
            if len(n)==2:
                pass
    return count

def check(listofstrings):
    dict={}
    for string in listofstrings:
        list1=[]
        list1[:0]=string
        if len(list1)==2:
            dict[1]=list1
        elif len(list1)==3:
            dict[7]=list1
        elif len(list1)==4:
            dict[4]=list1
        elif len(list1)==7:
            dict[8]=list1
        else:
            pass
    # 5: [2,3,5]
    # 6: [0,6,9]
    for string in listofstrings:
        list1=[]
        list1[:0]=string
        if len(list1)==5:
            listset=set(list1)
            common=len(list(listset.intersection(dict[1])))
            if common==2:
                dict[3]=list1
            elif common==1:
                common2=len(list(listset.intersection(dict[4])))
                if common2==2:
                    dict[2]=list1
                elif common2==3:
                    dict[5]=list1
                else:
                    pass
            else:
                pass
        elif len(list1)==6:
            listset=set(list1)
            common=len(list(listset.intersection(dict[7])))
            if common==2:
                dict[6]=list1
            elif common==3:
                common2=len(list(listset.intersection(dict[4])))
                if common2==3:
                    dict[0]=list1
                elif common2==4:
                    dict[9]=list1
                else:
                    pass
            else:
                pass
    return dict


def process2(listin,listout):
    for idx in range(len(listin)):
        templist=listin[idx].split()
        dictofvalues=check(templist)
        string1=listout[idx]
        list2=string1.split()
        for string in list2:
            letterlist=[]
            letterlist[:0]=string
            listset=set(letterlist)
            for value in list(dictofvalues.values()):
                count=0
                if len(value)==len(letterlist):
                    for l in value:
                        if l in letterlist:
                            count+=1
                if count==len(value):
                    list2[list2.index(string)]=list(dictofvalues.keys())[list(dictofvalues.values()).index(value)]
                    break
        listout[idx]=list2
    return listout


def addition(listoflists):
    number=0
    list2=[]
    for list in listoflists:
        number=list[0]*1000+list[1]*100+list[2]*10+list[3]
        list2.append(number)
    return sum(list2)

input1,input2=readfile('Day8_2021_input.txt')
output=process2(input2,input1)
print(addition(output))

