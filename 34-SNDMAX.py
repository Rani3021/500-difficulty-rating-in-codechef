# cook your dish here
N=int(input())
for _ in range(N):
    a,b,c=map(int,input().split())
    sec_max=sorted([a,b,c])[1]
    print(sec_max)
