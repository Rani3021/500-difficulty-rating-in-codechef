# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if x*y<=z*24*60:
        print("YES")
    else:
        print("NO")