# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if y>=x*3:
        print("YES")
    else:
        print("NO")