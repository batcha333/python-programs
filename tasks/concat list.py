l1=['M','na','i','Ke']
l2=['y','me','s','lly']
l=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if(i==j):
            l.append(l1[i]+l2[j])
print(l,end=" ")

    
