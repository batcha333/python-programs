str1='I am 25 years and 10 months old'.split(' ')
for i in str1:
    if(i.isnumeric()):
        print(i,end="")
