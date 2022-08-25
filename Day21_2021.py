
def turn(pos,score,count,dicevalue):
    count+=1
    pos=pos+dicevalue+(dicevalue+1)+(dicevalue+2)
    dicevalue+=3
    while pos>10:
        pos=pos-10
    score+=pos
    #print(count)
    if score>=1000:
        return count*3,count,dicevalue,pos,score
    else:
        return None,count,dicevalue,pos,score
        

dicevalue=1
p1_pos,p2_pos=6,9
p1_score,p2_score=0,0
count=0
step=None
while(step==None):
    step,count,dicevalue,p1_pos,p1_score=turn(p1_pos,p1_score,count,dicevalue)
    if step==None:
        step,count,dicevalue,p2_pos,p2_score=turn(p2_pos,p2_score,count,dicevalue)
print(step*min(p1_score,p2_score))
print('endcode')

