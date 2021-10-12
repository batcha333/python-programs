a=input('enter: ').split()
count=0
print(a)
for i in a:
    b=i[::-1]
    if(i==b):
        count=count+1
print(count)
