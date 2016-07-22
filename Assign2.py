def abc (x,y):
    xy=[]

    for a in range(0,x):
        xy.append([])
        for b in range(0,y):
            xy[a].append(a*b)
    return(xy)



msg=("Please enter no")
x=int(input(msg))
y=int(input(msg))
ab= abc(x,y)
print(ab)


