str="OceAnaCaDemy"
l=[]
m=[]
for i in str:
    if(ord(i)>96):
        l.append(i)
    else:
        m.append(i)
l.extend(m)
for i in l:
    print(i,end="")
        

