# cook your dish here
p=map(int,input().split())
c=0
for i in p:
    if i>=10:
        c+=1
print(c)