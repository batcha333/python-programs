a=int(input("enter: "))
sum=0
for i in range(1,a+1):
    sum+=i
    if(i!=a):
        print(i,end="+")
    else:
        print(i,"=",sum)

