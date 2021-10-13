str1="PYnative29@#8496"
str2=list(str1)
l=[]
sum=0
print(str2)
for i in range(len(str2)):
    if str2[i].isdigit():
        l.append(str2[i])
        sum+=int(str2[i])
print(sum)
print(sum/len(l))
