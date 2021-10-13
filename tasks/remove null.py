str1=['Emma','Jon',' ','Kelly',None,'eric',' ']
s=[]
for i in str1:
    if(i==' ')or(i==None):
        continue
        
    else:
        s.append(i)
print(s)
