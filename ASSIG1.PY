l=[]
lower= input("Please enter the lower range ")
upper= input("Please enter the upper range")
for i in range(int(lower),int(upper)):
    a=i
    if (a%7==0) and (a%5!=0):
        l.append(i)
print(l)





