a=int(input("Enter the num: "))
i=a
sqr=i*i
print(sqr)
x=[int(a) for a in str(sqr)]
print(x)
sum=0
for e in range(len(x)):
    sum+=x[e]
print(sum)
if(sum==i):
    print((i),"is a neon number" )
else:
    print((i),"is not a neon number")
