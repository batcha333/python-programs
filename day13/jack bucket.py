a=['H','F','B','A','C','L','K','G','V','C','B','I','U','K','F']
b="BLACKBUCK"
count=0
for i in range(len(b)):
    if b[i] in a:
        a.remove(b[i])
        count+=1
if(count==len(b)):
    print('yes')
else:
    print('No')
