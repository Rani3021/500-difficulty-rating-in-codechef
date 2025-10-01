# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x*3<y*2:
        print(x*3)
    else:
        print(y*2)