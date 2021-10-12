a=input("")
c=list(a.split())
d=input("enter: ")
l = []
for i in c:
    if(i.startswith(d)):
        print(i)
        l.append(i)
        print(l)
        
        
