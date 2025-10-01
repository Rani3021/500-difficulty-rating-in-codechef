# cook your dish here
t=int(input())
for _ in range(t):
    na,nb,nc=map(int,input().split())
    if na>nb+nc or nb>na+nc or nc>na+nb:
        print("YES")
    else:
        print("NO")