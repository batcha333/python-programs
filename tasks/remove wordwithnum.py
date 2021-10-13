str1='Emma25 is Data scientist50 and AI expert'
s=str1.split()
a=[]
for i in s:
    if any(chr.isalpha() for chr in i)and any(chr.isdigit() for chr in i):
        a.append(i)
for i in a:
    print(i)
