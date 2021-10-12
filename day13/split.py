bucket=[]
count=0
b=input("")
for i in b:
    bucket.append(i)
print(bucket)
a=input('word= ')
for i in b:
    if(a in bucket):
        count=1
if(count==1):
    print('yes')
else:
    print('no')
'''if(l in bucket):
        print('yes')'''
