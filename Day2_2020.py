from typing import Counter

def readfile(x):                            #function to read input file                
    claimlist=[]                            
    pw1=[]                                  #Counter dictionary of initial string from function convert
    f=open(x,'r')                           
    lines=f.readlines()                     
    for line in lines:                      
        limit,ch,pw=line.split()            #split from 1-3 a: abcde form to 1,3,a,abcde
        #pw1=convert(pw)                     
        ll,ul=limit.split('-')
        ch1=ch.replace(':','')              
        claim=[int(ll),int(ul),ch1,pw]     #list with lower limit, upper limit, character and counter dict
        claimlist.append(claim)             #list with all lists
    return claimlist        

def convert(list):                          #function to convert string to dict
    list1=[]
    list1[:0]=list
    cnt=Counter()
    for letter in list1:
        cnt[letter]+=1
    return list1

def check(list1):                                   #input claimlist
    flag=0                                          #counter for valid passwords
    m=0
    for li in list1:                                #li=[1,3,'a',Counter({'a':1, 'b':1, 'c':1, 'd':1, 'e':1})]
        if li[2] in li[3].keys():                   
            m=list(li[3].values())[list(li[3].keys()).index(li[2])]       #m uses value of previous iteration?????
            if ((m>=li[0]) and (m<=li[1])):
                flag+=1
        else:
            if li[0]==0:
                flag+=1
    return flag

def check2(l):
    count=0
    for item in l:
        str=item[3]
        if (str[item[0]-1]==item[2] and str[item[1]-1]!=item[2]) or (str[item[0]-1]!=item[2] and str[item[1]-1]==item[2]):
            count+=1
    return count

input=readfile('Day2_2020_input.txt')
print(len(input))
value=check2(input)
print(value)

