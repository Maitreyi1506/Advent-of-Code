def circle(n):
    arr=[0,2,1]
    idx=1
    for i in range(3,n+1):
        idx+=2
        if idx<=len(arr):
            pass
        elif idx>len(arr):
            idx-=len(arr)
        arr.insert(idx,i)
    print(arr)

circle(9)    